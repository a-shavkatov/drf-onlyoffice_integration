from datetime import timedelta

from django.conf import settings

from src.apps.services.minio.client import client


def get_file_presigned_url(my_object: str, expires_time=timedelta(minutes=5)) -> dict:
    bucket = settings.MINIO_STORAGE_MEDIA_BUCKET_NAME

    return client.get_presigned_url("GET", bucket, my_object, expires=expires_time)
