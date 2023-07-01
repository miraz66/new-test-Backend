from .models import Customer
from .serializers import CustomerSerializer

from django.http import JsonResponse

# Create your views here.


def Customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)

    return JsonResponse({"customers": serializer.data})
