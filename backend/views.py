from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.management.utils import get_random_secret_key

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.utils.caesar_cipher import caesar_cipher
from backend.utils.vigenere_cipher import vigenere_cipher
from backend.utils.random_numbers import generate_random_numbers


@csrf_protect
@api_view(['POST'])
@permission_classes([AllowAny,])
def generator_view(request):
    if request.method == 'POST':
        _secret_key = get_random_secret_key()

        response = {
            'key': _secret_key
        }

        return JsonResponse(response)

    return Response({"error": "Invalid request method."}, status=status.HTTP_400_BAD_REQUEST)


MAX_TEXT_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_NUM_COUNT = 1000  # 1000 numbers can be generated


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


@csrf_protect
@api_view(['POST'])
@permission_classes([AllowAny,])
def secure_random_numbers_view(request):
    if request.method == 'POST':
        try:
            # Extract data from the request
            min_value = request.data.get('min_value')
            max_value = request.data.get('max_value')
            count = request.data.get('count', 1)
            unique = request.data.get('unique', True)

            # Validate required fields
            if min_value is None or max_value is None:
                return Response({"error": "min_value and max_value are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Convert values to integers
            min_value = int(min_value)
            max_value = int(max_value)
            count = int(count)
            unique = bool(unique)

            if count > MAX_NUM_COUNT:
                return Response({"error": "count cannot be more than 1000"}, status=status.HTTP_400_BAD_REQUEST)
            elif count <= 0:
                return Response({"error": "count cannot be less or equal 0"}, status=status.HTTP_400_BAD_REQUEST)

            # Generate random numbers using the updated function
            random_numbers = generate_random_numbers(min_value, max_value, count, unique)

            # Return the result
            return Response({"random_numbers": random_numbers}, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"error": "Invalid request method."}, status=status.HTTP_400_BAD_REQUEST)
