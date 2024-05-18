from django.db import models
from gallery.models import Gallery
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    hero_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    hero_gallery = models.ForeignKey(Gallery, related_name='hero_galleries', on_delete=models.SET_NULL, null=True, blank=True)
    full_gallery = models.ForeignKey(Gallery, related_name='full_galleries', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, related_name='services', on_delete=models.CASCADE)
    service_image = models.ImageField(upload_to='service_images', null=True, blank=True)
    service_image_url = models.CharField(max_length=200, null=True, blank=True)

    
    def save(self, *args, **kwargs):
        # Ensure the image_file field has been set
        
        self.service_image_url = f'service_images/{self.service_image.name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
