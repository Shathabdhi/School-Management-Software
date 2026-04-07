from django.db import models

from .enum import ExamType, Grade


# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=255)
    accademic_year = models.ForeignKey(
        "academics.AcademicYear",
        on_delete=models.CASCADE,
        related_name="exams",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    exam_type = models.CharField(max_length=50, choices=(ExamType.choices))

    class Meta:
        db_table = "exams"
        unique_together = (("accademic_year", "name"),)

    def __str__(self):
        return self.name


class ExamSchedule(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="schedules")
    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
        related_name="exam_schedules",
    )
    exam_datetime = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    max_marks = models.PositiveIntegerField()
    pass_marks = models.PositiveIntegerField()

    class Meta:
        db_table = "exam_schedules"
        unique_together = (("exam", "class_subject"),)

    def __str__(self):
        return f"{self.exam.name} - {self.class_subject.class_assigned.name} - {self.exam_datetime}"


class ExamResult(models.Model):
    exam_schedule = models.ForeignKey(
        ExamSchedule, on_delete=models.CASCADE, related_name="results"
    )
    student = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="exam_results"
    )
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5, choices=Grade.choices)
    remarks = models.TextField(blank=True, null=True)
    is_absent = models.BooleanField(default=False)

    class Meta:
        db_table = "exam_results"
        unique_together = (("exam_schedule", "student"),)

    def __str__(self):
        return f"{self.student.user.name} - {self.exam_schedule.exam.name} - {self.marks_obtained}"
