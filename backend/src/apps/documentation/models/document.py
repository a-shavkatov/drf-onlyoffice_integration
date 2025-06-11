from django.db import models

import uuid


def upload_path(instance, filename):
    return f"document/{instance.id}/{filename}"


# Create your models here.
class Document(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.title
