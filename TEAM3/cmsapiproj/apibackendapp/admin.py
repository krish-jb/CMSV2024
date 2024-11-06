from django.contrib import admin
from .models import (
    Medicine,
    Appointment,
    Doctor,
    Patient,
    Staff,
    Specialization,
    Role,
    MedicineCategory,
    Membership,
)

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Specialization)
admin.site.register(Role)
admin.site.register(MedicineCategory)
admin.site.register(Membership)
