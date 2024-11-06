from rest_framework import serializers
from .models import MedicineStock
from datetime import date

class MedicineStockSerializer(serializers.ModelSerializer):
    class Meta :
        model = MedicineStock
        fields = '__all__'