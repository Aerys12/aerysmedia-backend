from rest_framework import generics
from service.models import Service
from rest_framework.permissions import IsAuthenticated
from service.serializers import service_serializer


class ViewServices(generics.ListAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = service_serializer.SimpleServiceSerializer


    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)