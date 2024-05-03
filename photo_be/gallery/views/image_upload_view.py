from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from gallery.serializers import image_serializer
from gallery.models import Gallery

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]  # Ensuring that the user is authenticated

    def post(self, request, gallery_id):
        try:
            gallery = Gallery.objects.get(id=gallery_id, owner=request.user)  # Ensure user owns the gallery
        except Gallery.DoesNotExist:
            return Response({"error": "Gallery not found or not accessible."}, status=status.HTTP_404_NOT_FOUND)
        
        files = request.FILES.getlist('image_files')
        if not files:
            return Response({"error": "No images uploaded."}, status=status.HTTP_400_BAD_REQUEST)
        
        images = []
        for file in files:
            data = {
                'gallery': gallery.id,
                'image_file': file,
                'title': file.name,  
            }
            serializer = image_serializer.ImageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                images.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(images, status=status.HTTP_201_CREATED)
