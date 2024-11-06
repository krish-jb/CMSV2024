from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import filters
class DoctorViewSet(viewsets.ModelViewSet):
  queryset=Doctor.objects.all()
  serializer_class=DoctorSerializer
  filter_backends=[filters.SearchFilter]
  search_fields=['DoctorId']