from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.management.utils import get_random_secret_key

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.utils.caesar_cipher import caesar_cipher
from backend.utils.vigenere_cipher import vigenere_cipher


@csrf_protect
@api_view(['POST'])
@permission_classes([AllowAny,])
def generator_view(request):
    _secret_key = get_random_secret_key()

    response = {
        'key': _secret_key
    }

    return JsonResponse(response)


MAX_TEXT_SIZE = 10 * 1024 * 1024  # 10 MB

@csrf_protect
@api_view(['POST'])
@permission_classes([AllowAny,])
def caesar_cipher_view(request):
    if request.method == 'POST':
        text = request.data.get('text', '')
        shift = request.data.get('shift', 3)
        mode = request.data.get('mode', 'encrypt')

        if len(text.encode('utf-8')) > MAX_TEXT_SIZE:
            return Response({"error": "Text size exceeds the allowed limit."}, status=status.HTTP_400_BAD_REQUEST)

        result = caesar_cipher(text, shift=shift, mode=mode)

        return Response({"result": result}, status=status.HTTP_200_OK)

    return Response({"error": "Invalid request method."}, status=status.HTTP_400_BAD_REQUEST)


@csrf_protect
@api_view(['POST'])
@permission_classes([AllowAny,])
def vigenere_cipher_view(request):
    if request.method == 'POST':
        text = request.data.get('text', '')
        key = request.data.get('key', '')
        mode = request.data.get('mode', 'encrypt')

        # Validate text size
        if len(text.encode('utf-8')) > MAX_TEXT_SIZE:
            return Response({"error": "Text size exceeds the allowed limit."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate key (must not be empty)
        if not key:
            return Response({"error": "Key is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Perform Vigenère cipher operation
        result = vigenere_cipher(text, key=key, mode=mode)

        return Response({"result": result}, status=status.HTTP_200_OK)

    return Response({"error": "Invalid request method."}, status=status.HTTP_400_BAD_REQUEST)
