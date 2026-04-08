from rest_framework import serializers

from apps.accounts.serializers import TeacherSerializer

from .models import (
    AcademicYear,
    Class,
    ClassSubject,
    Department,
    School,
    Subject,
    Timetable,
)


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "id",
            "name",
            "address",
            "phone",
            "contact_email",
            "established_date",
            "logo",
        ]
        read_only_fields = ["id"]


class AcademicYearSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = AcademicYear

        fields = [
            "id",
            "school",
            "name",
            "start_date",
            "end_date",
            "is_active",
        ]

        read_only_fields = ["id"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            "id",
            "department",
            "name",
            "code",
            "description",
            "credits",
            "subject_type",
        ]
        read_only_fields = ["id"]


class DepartmentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Department

        fields = ["id", "school", "name", "code", "description"]
        read_only_fields = ["id"]


class ClassSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    academic_year = AcademicYearSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ["id", "department", "academic_year", "name", "section", "capacity"]
        read_only_fields = ["id"]


class ClassSubjectSerializer(serializers.ModelSerializer):
    class_assigned = ClassSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = ClassSubject

        fields = [
            "id",
            "class_assigned",
            "subject",
            "teacher",
        ]
        read_only_fields = ["id"]


class TimetableSerializer(serializers.ModelSerializer):
    class_subject = ClassSubjectSerializer(read_only=True)

    class Meta:
        model = Timetable

        fields = [
            "id",
            "class_subject",
            "day_of_week",
            "start_time",
            "end_time",
            "room",
        ]
        read_only_fields = ["id"]
