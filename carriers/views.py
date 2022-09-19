from .models import Carrier
from .serializers import CarrierSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class CarrierList(ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

class CarrierDetail(RetrieveUpdateDestroyAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer