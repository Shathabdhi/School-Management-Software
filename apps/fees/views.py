from rest_framework import viewsets

from .models import FeePayment, FeeStructure
from .serializers import FeePaymentSerializer, FeeStructureSerializer


# Create your views here.
class FeeStructureViewSet(viewsets.ModelViewSet):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer


class FeePaymentViewSet(viewsets.ModelViewSet):
    queryset = FeePayment.objects.all()
    serializer_class = FeePaymentSerializer
