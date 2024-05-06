from rest_framework import serializers
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True}}