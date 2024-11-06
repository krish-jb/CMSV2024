from django.shortcuts import render
from .serializers import MedicinePrescriptionSerializer
from .models import MedicinePrescription
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.


class MedicineCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer
