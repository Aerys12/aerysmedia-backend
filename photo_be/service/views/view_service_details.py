from rest_framework import generics
from service.models import Service
from rest_framework.permissions import IsAuthenticated
from service.serializers import service_serializer

class ServiceDetails(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = service_serializer.ServiceSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        service_id = self.kwargs['id']
        return Service.objects.filter(owner=self.request.user, id=service_id)
    
    