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

    def __str__(self):
        return self.name
