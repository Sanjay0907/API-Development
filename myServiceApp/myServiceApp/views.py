import imp
from django.http import JsonResponse
from .models import services
from .serializers import ServicesSerializer


def servicesList(request):
    # Get all Services
    # Serialize them
    # Return JSON
    serviceS = services.objects.all()
    serializer = ServicesSerializer(serviceS, many=True)
    return JsonResponse(serializer.data, safe=False)
