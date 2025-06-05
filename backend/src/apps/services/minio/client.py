from django.conf import settings
from minio import Minio

client = Minio(
    endpoint=settings.MINIO_STORAGE_ENDPOINT,
    access_key=settings.MINIO_STORAGE_ACCESS_KEY,
    secret_key=settings.MINIO_STORAGE_SECRET_KEY,
    secure=settings.MINIO_STORAGE_USE_HTTPS,
)
