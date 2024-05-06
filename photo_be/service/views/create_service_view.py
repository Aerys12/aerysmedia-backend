from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from service.models import Service
from service.serializers import service_serializer