from rest_framework import serializers

from apps.academics.serializers import AcademicYearSerializer, ClassSerializer
from apps.accounts.serializers import StudentSerializer

from .models import FeePayment, FeeStructure


class FeeStructureSerializer(serializers.ModelSerializer):
    academic_year = AcademicYearSerializer(read_only=True)
    class_assigned = ClassSerializer(read_only=True)

    class Meta:
        model = FeeStructure
        fields = [
            "id",
            "academic_year",
            "class_assigned",
            "fee_type",
            "amount",
            "due_date",
            "is_optional",
            "description",
        ]
        read_only_fields = ["id"]


class FeePaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    fee_structure = FeeStructureSerializer(read_only=True)

    class Meta:
        model = FeePayment
        fields = [
            "id",
            "student",
            "fee_structure",
            "amount_paid",
            "payment_date",
            "payment_method",
            "transaction_id",
            "receipt_number",
            "status",
            "notes",
        ]
        read_only_fields = ["id"]
