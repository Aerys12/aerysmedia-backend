from rest_framework import serializers
from gallery.models import Gallery
from service.serializers.service_serializer import SimpleServiceSerializer

class GallerySerializer(serializers.ModelSerializer):
    service = SimpleServiceSerializer(read_only=True)
    class Meta:
        model = Gallery
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}

