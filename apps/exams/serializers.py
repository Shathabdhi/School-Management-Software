from rest_framework import serializers

from apps.academics.serializers import (
    AcademicYearSerializer,
    ClassSubjectSerializer,
)
from apps.accounts.serializers import StudentSerializer

from .models import Exam, ExamResult, ExamSchedule


class ExamSerializer(serializers.ModelSerializer):
    academic_year = AcademicYearSerializer(read_only=True)

    class Meta:
        model = Exam
        fields = ["id", "academic_year", "start_date", "end_date", "exam_type"]
        read_only_fields = ["id"]


class ExamScheduleSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)
    class_subject = ClassSubjectSerializer(read_only=True)

    class Meta:
        model = ExamSchedule
        fields = [
            "id",
            "exam",
            "class_subject",
            "exam_datetime",
            "duration_minutes",
            "max_marks",
            "pass_marks",
        ]
        read_only_fields = ["id"]


class ExamResultSerializer(serializers.ModelSerializer):
    exam_schedule = ExamScheduleSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = ExamResult
        fields = ["id", "marks_obtained", "grade", "remarks", "is_absent"]
        read_only_fields = ["id"]
