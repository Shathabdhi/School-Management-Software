from django.db import models

class ExamType(models.TextChoices):
    MIDTERM = "midterm", "Midterm"
    FINAL = "final", "Final"
    QUIZ = "quiz", "Quiz"

class Grade(models.TextChoices):
    A = "A", "A"
    B = "B", "B"
    C = "C", "C"
    D = "D", "D"
    F = "F", "F"