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
    LabTest,
    LabTestPrescription,
    LabTestCategory,
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
admin.site.register(LabTest)
admin.site.register(LabTestCategory)
admin.site.register(LabTestPrescription)
