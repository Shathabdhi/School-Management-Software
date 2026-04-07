from django.db import models

from .enum import Audience

# Create your models here.
class Notice(models.Model):
    school = models.ForeignKey(
        "academics.School", on_delete=models.CASCADE, related_name="notices"
    )
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, related_name="created_notices"
    )
    audience = models.CharField(max_length=20, choices=(Audience.choices))
    title = models.CharField(max_length=255)
    attachment = models.FileField(upload_to="notices/attachments/", blank=True, null=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "notices"

    def __str__(self):
        return self.title