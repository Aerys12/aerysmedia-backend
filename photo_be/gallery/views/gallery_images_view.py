from gallery.models import Image
from gallery.serializers import image_serializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class GalleryImagesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = image_serializer.ImageSerializer
    

    def get_queryset(self):
        gallery_id = self.kwargs['gallery_id']
        return Image.objects.filter(gallery=gallery_id)