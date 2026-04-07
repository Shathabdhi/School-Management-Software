from django.db import models

from .enum import AttendanceStatus


# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey(
        "accounts.Student",
        on_delete=models.CASCADE,
        related_name="attendances",
    )
    class_subject = models.ForeignKey(
        "academics.ClassSubject",
        on_delete=models.CASCADE,
        related_name="attendances",
    )
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(AttendanceStatus.choices))
    remarks = models.TextField(blank=True, null=True)
    marked_by = models.ForeignKey(
        "accounts.Teacher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="marked_attendances",
    )

    class Meta:
        db_table = "attendances"
        unique_together = (("student", "date", "class_subject"),)

    def __str__(self):
        return f"{self.student.user.name} - {self.class_subject.class_assigned.name} - {self.date} - {self.status}"
