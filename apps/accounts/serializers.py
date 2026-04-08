from rest_framework import serializers

from .models import Parent, Student, Teacher, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "mobile_number",
            "role",
            "gender",
            "is_active",
            "added_time",
        ]  # which fields to include

        read_only_fields = ["id", "is_active", "added_time"]

        extra_kwargs = {
            "mobile_number": {"write_only": True},  # can be written but never returned
            "email": {"required": False},  # not mandatory
        }


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer for user details

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user",
            "department",
            "emp_id",
            "qualification",
            "specialization",
            "joining_date",
            "is_class_teacher",
        ]

        read_only_fields = ["id"]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer for user details

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "class_assigned",
            "roll_number",
            "admission_number",
            "date_of_birth",
            "gender",
            "blood_group",
            "admission_date",
            "address",
        ]

        read_only_fields = ["id", "admission_number"]


class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer for user details

    class Meta:
        model = Parent
        fields = [
            "id",
            "user",
            "occupation",
            "address",
            "alternative_phone",
        ]

        read_only_fields = ["id"]


class TeacherCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # not read_only — accepts input

    class Meta:
        model = Teacher
        fields = [
            "user",
            "department",
            "emp_id",
            "qualification",
            "specialization",
            "joining_date",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")  # separate user data
        # create the user first
        user_data["role"] = "teacher"  # force role
        user = User.objects.create_user(**user_data)  # create user
        # then create the teacher profile linked to that user
        teacher = Teacher.objects.create(user=user, **validated_data)  # create teacher
        return teacher

    def update(self, instance, validated_data):
        # pop user data if present
        user_data = validated_data.pop("user", {})  # {} default if not provided

        # update user fields
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()

        # update profile fields
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class StudentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = [
            "user",
            "class_assigned",
            "roll_number",
            "admission_number",
            "date_of_birth",
            "gender",
            "blood_group",
            "admission_date",
            "address",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")  # separate user data
        # create the user first
        user_data["role"] = "student"  # force role
        user = User.objects.create_user(**user_data)  # create user
        # then create the student profile linked to that user
        student = Student.objects.create(user=user, **validated_data)  # create student
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ParentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # not read_only — accepts input

    class Meta:
        model = Parent
        fields = [
            "user",
            "occupation",
            "address",
            "alternative_phone",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data["role"] = "parent"  # force role
        user = User.objects.create_user(**user_data)  # create user
        parent = Parent.objects.create(user=user, **validated_data)  # create parent
        return parent

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})

        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
