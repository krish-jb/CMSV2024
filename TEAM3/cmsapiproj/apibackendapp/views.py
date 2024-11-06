from .serializers import MedicinePrescriptionSerializer, LabTestPrescriptionSerializer
from .models import MedicinePrescription, LabTestPrescription
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.


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
