from .serializers import (
    MedicinePrescriptionSerializer,
    LabTestPrescriptionSerializer,
    DoctorSerializer,
    MedicineStockSerializer,
    MedicineSerializer,
    MedicinePrescriptionSerializer
)
from .models import MedicinePrescription, LabTestPrescription
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Doctor, MedicineStock, Medicine
from rest_framework import filters

# Create your views here.

class MedicineStockViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer


class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Medicine prescription created successfully."},
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Medicine Prescription updated successfully."},
            status=status.HTTP_200_OK,
        )


class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = LabTestPrescription.objects.all()
    serializer_class = LabTestPrescriptionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Lab Test prescription createed successfully."},
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Lab Test Prescription updated successfully."},
            status=status.HTTP_200_OK,
        )


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['DoctorId']



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