from rest_framework import serializers

from src.apps.services.minio.utils import get_file_presigned_url
from src.apps.documentation.models import Document, Template
from src.apps.user.serializers import UserSerializer

from django.core.files.base import ContentFile
import os


class DocumentCreateSerializer(serializers.ModelSerializer):
    template = serializers.PrimaryKeyRelatedField(
        queryset=Template.objects.all(), write_only=True
    )

    class Meta:
        model = Document
        fields = ("id", "title", "template")
        read_only_fields = ("id",)
        extra_kwargs = {"title": {"write_only": True}}

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        template = validated_data.pop("template")
        document = super().create(validated_data)

        file_name = os.path.basename(template.file.name)
        document.file.save(file_name, ContentFile(template.file.read()), save=True)
        document.save(update_fields=["file"])
        return document


class DocumentListSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        exclude = ("file",)

    def get_file_url(self, obj):
        if obj.file:
            return get_file_presigned_url(obj.file.name)
