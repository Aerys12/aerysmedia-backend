from gallery.models import Gallery
from gallery.serializers import gallery_serializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class GalleryUpdateView(generics.UpdateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = gallery_serializer.GallerySerializer
    permission_classes = [IsAuthenticated]

  

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
