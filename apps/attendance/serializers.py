from rest_framework import serializers

from apps.academics.serializers import ClassSubjectSerializer
from apps.accounts.serializers import StudentSerializer, TeacherSerializer

from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class_subject = ClassSubjectSerializer(read_only=True)
    marked_by = TeacherSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = [
            "id",
            "student",
            "class_subject",
            "date",
            "status",
            "remarks",
            "marked_by",
        ]

        read_only_fields = ["id"]
