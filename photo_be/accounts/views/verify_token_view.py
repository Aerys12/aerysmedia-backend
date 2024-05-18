# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def verify_token(request):
    authorization_header = request.headers.get('Authorization')
    if authorization_header is not None:
        token_key = authorization_header.split(' ')[1]
        try:
            token = Token.objects.get(key=token_key)
            return Response({'valid': True})
        except Token.DoesNotExist:
            return Response({'valid': False}, status=401)
    else:
        return Response({'error': 'Authorization header not found'}, status=400)
