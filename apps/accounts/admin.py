from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    # What columns show in the list view
    list_display = ("email", "name", "role", "is_active", "is_staff")

    # Which fields can be searched
    search_fields = ("email", "name", "mobile_number")

    # Filter sidebar
    list_filter = ("role", "is_active", "is_staff", "gender")

    # Default ordering
    ordering = ("email",)

    # Fields shown when editing an existing user
    fieldsets = (
        ("Login Info", {"fields": ("email", "mobile_number", "password")}),
        ("Personal Info", {"fields": ("name", "gender", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "added_time")}),
    )

    # Fields shown when creating a new user from admin
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "mobile_number",
                    "name",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    # added_time is auto set so it can't be edited
    readonly_fields = ("last_login", "added_time")


admin.site.register(User, CustomUserAdmin)
