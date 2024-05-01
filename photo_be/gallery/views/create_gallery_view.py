from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gallery.serializers import gallery_serializer
from rest_framework.permissions import IsAuthenticated

class GalleryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = gallery_serializer.GallerySerializer(data=request.data)
        if serializer.is_valid():
            # Manually add the authenticated user as the owner
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
