from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from gallery.models import Gallery
from gallery.serializers import gallery_serializer
from django.shortcuts import get_object_or_404

class GalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = gallery_serializer.GallerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Gallery.objects.filter(owner=self.request.user)
