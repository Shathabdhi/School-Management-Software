from django.db import models


class SubjectType(models.TextChoices):
    CORE = "core", "Core"
    ELECTIVE = "elective", "Elective"
    LAB = "lab", "Lab"


class Day(models.TextChoices):
    MONDAY = "monday", "Monday"
    TUESDAY = "tuesday", "Tuesday"
    WEDNESDAY = "wednesday", "Wednesday"
    THURSDAY = "thursday", "Thursday"
    FRIDAY = "friday", "Friday"
    SATURDAY = "saturday", "Saturday"
    SUNDAY = "sunday", "Sunday"
