from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import MedicineStock
from .serializers import MedicineStockSerializer

# Create your views here.

class MedicineStockViewSet(viewsets.ModelViewSet):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer
