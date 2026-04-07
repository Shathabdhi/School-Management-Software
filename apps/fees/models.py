from django.db import models

from .enum import FeeType, PaymentMethod, PaymentStatus


# Create your models here.
class FeeStructure(models.Model):
    academic_year = models.ForeignKey(
        "academics.AcademicYear",
        on_delete=models.CASCADE,
        related_name="fee_structures",
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="fee_structures",
    )
    fee_type = models.CharField(max_length=50, choices=(FeeType.choices))
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_optional = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "fee_structures"
        unique_together = (("academic_year", "class_assigned", "fee_type"),)

    def __str__(self):
        return f"{self.class_assigned.name} - {self.amount} - {self.due_date}"


class FeePayment(models.Model):
    student = models.ForeignKey(
        "accounts.Student",
        on_delete=models.SET_NULL,
        related_name="fee_payments",
        null=True,
        blank=True,
    )
    fee_structure = models.ForeignKey(
        FeeStructure, on_delete=models.SET_NULL, null=True, related_name="fee_payments"
    )
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=(PaymentMethod.choices))
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    receipt_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20, default="paid", choices=(PaymentStatus.choices)
    )
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "fee_payments"

    def __str__(self):
        return f"{self.student.user.name} - {self.fee_structure.class_assigned.name} - {self.amount_paid}"
