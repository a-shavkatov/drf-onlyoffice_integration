from rest_framework import serializers

from src.apps.services.minio.utils import get_file_presigned_url
from src.apps.user.serializers import UserSerializer
from src.apps.documentation.models import Document


class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("id", "title", "file")
        read_only_fields = ("id",)
        extra_kwargs = {
            "file": {"write_only": True},
            "title": {"write_only": True},
        }

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        file = validated_data.pop("file")
        document = super().create(validated_data)
        document.file = file
        document.save(update_fields=["file"])

        return document


class DocumentListSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        exclude = ("file",)

    def get_file_url(self, obj):
        return get_file_presigned_url(obj.file.name)
