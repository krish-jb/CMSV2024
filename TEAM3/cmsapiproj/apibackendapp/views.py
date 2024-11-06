from rest_framework import viewsets
from .models import Medicine
from .serializers import MedicineSerializer , MedicinePrescriptionSerializer
from rest_framework.permissions import AllowAny

class MedicineViewSets(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicinePrescriptionViewSets(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Medicine.objects.all()
    serializer_class = MedicinePrescriptionSerializer


# class PatientViewSets(viewsets.ModelViewSet):
#     queryset = Medicine.objects.all()
#     serializer_class = PatientSerializer

# class MedicineStockViewSets(viewsets.ModelViewSet):
#     queryset = Medicine.objects.all()
#     serializer_class = MedicineStockSerializer