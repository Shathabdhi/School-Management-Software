from rest_framework import serializers

from apps.academics.serializers import SchoolSerializer
from apps.accounts.serializers import UserSerializer

from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Notice
        fields = [
            "id",
            "school",
            "created_by",
            "audience",
            "title",
            "attachment",
            "content",
            "is_published",
            "published_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id"]
