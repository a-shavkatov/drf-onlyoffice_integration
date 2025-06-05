from rest_framework import serializers

from src.apps.documentation.models import Template
from src.apps.services.minio.utils import get_file_presigned_url


class TemplateSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Template
        exclude = ("file",)

    def get_file_url(self, obj):
        return get_file_presigned_url(obj.file.name)
