from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import register_serializer

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = register_serializer.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

