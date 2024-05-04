from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image
import boto3
from django.conf import settings
from urllib.parse import urlparse

@receiver(post_delete, sender=Image)
def delete_file_from_s3(sender, instance, using, **kwargs):
    if instance.image_file:
        # Parse the URL to extract the S3 key
        url = urlparse(instance.image_file.url)
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        key = url.path.lstrip('/')  # Removes the leading slash

        # Initialize S3 client
        s3_client = boto3.client('s3',
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 region_name=settings.AWS_REGION_NAME)

        # Delete the object from S3
        s3_client.delete_object(Bucket=bucket_name, Key=key)

