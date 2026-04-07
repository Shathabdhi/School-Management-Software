from django.db import models


class Audience(models.TextChoices):
    STUDENTS = "students", "Students"
    TEACHERS = "teachers", "Teachers"
    PARENTS = "parents", "Parents"
    STAFF = "staff", "Staff"
    ALL = "all", "All"
