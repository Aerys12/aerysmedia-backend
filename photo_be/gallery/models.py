from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid


def gallery_image_path(instance, filename):
    # Slugify the gallery title to create a web-friendly URL
    gallery_name_slug = slugify(instance.gallery.title)
    # Extract the file extension from the original file name
    ext = filename.split('.')[-1]
    # Create a unique filename using UUID
    unique_filename = f'{uuid.uuid4()}.{ext}'
    # Return the path with the gallery name slug and the unique filename
    return f'{gallery_name_slug}/{unique_filename}'



User = get_user_model()
# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='galleries', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    service = models.ForeignKey('service.Service', related_name='service_galleries', on_delete=models.CASCADE, null=True, blank=True)

    

    def __str__(self):
        return self.title


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to=gallery_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure the image_file field has been set
        if self.image_file and not self.image_file._committed:
            # Update the title based on the output from the upload_to function
            self.title = gallery_image_path(self, self.image_file.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title if self.title else "Image %s" % self.id
