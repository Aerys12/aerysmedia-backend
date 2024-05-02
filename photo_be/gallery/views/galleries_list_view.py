from gallery.models import Gallery
from gallery.serializers import gallery_serializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class GalleryListView(generics.ListAPIView):
    """
    API endpoint that allows galleries to be viewed.
    """
    queryset = Gallery.objects.all()
    serializer_class = gallery_serializer.GallerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Gallery.objects.filter(owner=self.request.user)
