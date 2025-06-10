from django.core.files.base import ContentFile
from rest_framework import serializers
import requests

from src.apps.documentation.models import Document
import os


class StatusKeys:
    NEW_USER_CONNECTED = 1
    READY_FOR_SAVING = 2
    SAVING_ERROR = 3
    NO_CHANGES = 4
    FORCE_SAVE_STATUS = 6
    CORRUPTED_STATUS = 7

    CHOICES = [
        (NEW_USER_CONNECTED, "Connected"),
        (READY_FOR_SAVING, "READY FOR SAVING"),
        (SAVING_ERROR, "SAVING ERROR"),
        (NO_CHANGES, "NO_CHANGES"),
        (FORCE_SAVE_STATUS, "FORCE SAVE STATUS"),
        (CORRUPTED_STATUS, "CORRUPTED_STATUS"),
    ]


class ResponseStatuses:
    SUCCESS = 0
    ERROR = 1


class CallBackSerializer(serializers.Serializer):
    key = serializers.CharField(write_only=True)
    status = serializers.ChoiceField(choices=StatusKeys.CHOICES, write_only=True)
    url = serializers.URLField(required=False, write_only=True)
    error = serializers.IntegerField(read_only=True)

    def validate(self, attrs):
        error_messages_mapping = {
            StatusKeys.SAVING_ERROR: "Saving error occurred",
            StatusKeys.CORRUPTED_STATUS: "File is corrupted",
        }

        error_message = error_messages_mapping.get(attrs["status"])
        if error_message:
            raise serializers.ValidationError(error_message)

        try:
            document = Document.objects.get(key=attrs["key"])
            attrs["document"] = document
        except Document.DoesNotExist:
            raise serializers.ValidationError("Document does not exists.")

        return super().validate(attrs)

    def create(self, validated_data):
        status = validated_data["status"]
        document = validated_data["document"]

        if status == StatusKeys.NO_CHANGES or status == StatusKeys.NEW_USER_CONNECTED:
            return {"error": ResponseStatuses.SUCCESS}

        response = requests.get(validated_data["url"])
        if response.status_code == 200:
            document.file.save(
                os.path.basename(document.file.name),
                ContentFile(response.content),
                save=True,
            )

            return {"error": ResponseStatuses.SUCCESS}

        return {"error": ResponseStatuses.ERROR}
