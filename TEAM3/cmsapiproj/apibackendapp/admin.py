from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import MedicineStock, Medicine, MedicinePrescription, MedicineCategory

# Register your models here.
admin.site.register(MedicineStock)
admin.site.register(Medicine)
admin.site.register(MedicinePrescription)
admin.site.register(MedicineCategory)
