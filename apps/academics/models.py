from django.db import models

from .enum import Day, SubjectType

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    contact_email = models.EmailField(max_length=255)
    established_date = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to="school/logos/", blank=True, null=True)

    class Meta:
        db_table = "schools"

    def __str__(self):
        return self.name


class Department(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="departments"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "departments"
        unique_together = ("school", "code")

    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="academic_years"
    )
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "academic_years"
        unique_together = ("school", "name")

    def __str__(self):
        return self.name


class Class(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="classes",
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name="classes",
    )
    name = models.CharField(max_length=255)
    section = models.CharField(max_length=10, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=30)

    class Meta:
        db_table = "classes"
        unique_together = ("academic_year", "name", "section")

    def __str__(self):
        return self.name


class Subject(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subjects",
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    credits = models.PositiveIntegerField(default=3)
    subject_type = models.CharField(
        max_length=50,
        choices=SubjectType.choices,
        default=SubjectType.CORE,
    )

    class Meta:
        db_table = "subjects"
        unique_together = ("department", "code")

    def __str__(self):
        return self.name


class ClassSubject(models.Model):
    class_assigned = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name="class_subjects"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="class_subjects"
    )
    teacher = models.ForeignKey(
        "accounts.Teacher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="class_subjects",
    )

    class Meta:
        db_table = "class_subjects"
        unique_together = ("class_assigned", "subject")

    def __str__(self):
        return f"{self.class_assigned.name} - {self.subject.name}"


class Timetable(models.Model):
    class_subject = models.ForeignKey(
        ClassSubject, on_delete=models.CASCADE, related_name="timetables"
    )
    day_of_week = models.CharField(
        max_length=10,
        choices=Day.choices,
        default=Day.MONDAY,
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "timetables"
        unique_together = ("class_subject", "day_of_week", "start_time")

    def __str__(self):
        return f"{self.class_subject.class_assigned.name} - {self.class_subject.subject.name} ({self.day_of_week})"
