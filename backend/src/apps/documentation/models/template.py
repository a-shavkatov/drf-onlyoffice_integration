from django.db import models


def upload_path(instance, filename):
    return f"template/{instance.id}/{filename}"


class Template(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=upload_path)

    def __str__(self):
        return self.name
