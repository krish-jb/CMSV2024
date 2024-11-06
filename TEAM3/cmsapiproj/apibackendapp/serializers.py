from rest_framework import serializers
from .models import MedicinePrescription, LabTestPrescription, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    FREQUENCY_CHOICES = [("once_a_day", "Once a day"), ("twice_a_day", "Twice a day")]

    Frequency = serializers.ChoiceField(choices=FREQUENCY_CHOICES)

    class Meta:
        model = MedicinePrescription
        fields = (
            "AppointmentId",
            "MedicineId",
            "Dosage",
            "Frequency",
        )


class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestPrescription
        fields = ("AppointmentId", "LabTestId", "LabTestValue", "Remarks")
