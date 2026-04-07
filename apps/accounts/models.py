from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from .enum import Gender, Relations


class Role(models.TextChoices):
    STUDENT = "student", "Student"
    TEACHER = "teacher", "Teacher"
    ADMIN = "admin", "Admin"
    PARENT = "parent", "Parent"


class UserManager(BaseUserManager):
    def create_user(self, email=None, mobile_number=None, **extra_fields):
        if not email and not mobile_number:
            raise ValueError("User must have at least an email or a mobile number")
        if email:
            email = self.normalize_email(email)
            extra_fields["email"] = email
        if mobile_number:
            extra_fields["mobile_number"] = mobile_number
        user = self.model(**extra_fields)
        user.set_unusable_password()  # No password use only OTP, so set unusable password
        # No password use only OTP, so no set_password here
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Superuser must have an email address")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        user = self.model(email=email, **extra_fields)
        # For admin login, you might still want a password for security
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # user Contact details
    name = models.CharField(max_length=255)
    added_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    gender = models.CharField(
        choices=Gender.choices, max_length=10, blank=True, null=True
    )
    role = models.CharField(choices=Role.choices, max_length=20)

    # Auth/system fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.name} ({self.role})"


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher_profile"
    )
    department = models.ForeignKey(
        "academics.Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="teachers",
    )
    emp_id = models.CharField(max_length=100, unique=True)
    qualification = models.CharField(max_length=255, blank=True)
    specialization = models.CharField(max_length=255, blank=True)
    joining_date = models.DateField()
    is_class_teacher = models.BooleanField(default=False)

    class Meta:
        db_table = "teachers"

    def __str__(self):
        return f"{self.user.name} ({self.user.role})"


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
    )
    roll_number = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=Gender.choices)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    admission_date = models.DateField()
    address = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "students"
        unique_together = (("class_assigned", "roll_number"),)

    def __str__(self):
        return f"{self.user.name} ({self.user.role})"


class Parent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="parent_profile"
    )
    occupation = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    alternative_phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "parents"

    def __str__(self):
        return f"{self.user.name} ({self.user.role})"


class StudentParent(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student_parents"
    )
    parent = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name="parent_students"
    )
    relation = models.CharField(max_length=50, choices=Relations.choices)
    is_primary_contact = models.BooleanField(default=False)

    class Meta:
        db_table = "student_parents"
        unique_together = (("student", "parent"),)

    def __str__(self):
        return f"{self.student.user.name} - {self.parent.user.name}"
