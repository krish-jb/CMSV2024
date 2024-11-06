from django.contrib import admin
from .models import Medicine , Patient , MedicineStock , MedicinePrescription
#register the department model to the admin interface
admin.site.register(Medicine)
# admin.site.register(Patient)
# admin.site.register(MedicineStock)
admin.site.register(MedicinePrescription)