from rest_framework import serializers
from gallery.models import Gallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}