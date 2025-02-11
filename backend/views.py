from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.management.utils import get_random_secret_key

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny,])
def generator_view(request):
    """Returns randomly generated Django Secret Key using JSONResponse"""

    _secret_key = get_random_secret_key()

    response = {
        'key': _secret_key
    }

    return JsonResponse(response)
