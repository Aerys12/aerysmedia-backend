from gallery.models import Image
from gallery.serializers import image_serializer
from rest_framework import generics

class ImageDeleteView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = image_serializer.ImageSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'image_id'


    def get_queryset(self):
        return self.queryset.filter(gallery__owner=self.request.user)