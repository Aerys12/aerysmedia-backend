from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

def gallery_image_path(instance, filename):
    # Slugify the gallery title to create a web-friendly URL
    gallery_name_slug = slugify(instance.gallery.title)
    # Return the path with the gallery name and filename
    return f'{gallery_name_slug}/{filename}'


User = get_user_model()
# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='galleries', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to=gallery_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title if self.title else "Image %s" % self.id
