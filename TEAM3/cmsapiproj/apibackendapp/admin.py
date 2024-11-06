from django.contrib import admin

# Register your models here.

from .models import (
    Role,
    MedicineCategory,
    Staff,
    Specialization,
    Doctor,
    Membership,
    Patient,
    Consultation,
    Appointment,
    LabTest,
    LabTestCategory,
    LabTestPrescription,
    MedicineStock,
    Medicine,
    MedicinePrescription
)

admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(Specialization)
admin.site.register(MedicineStock)
admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(Membership)
admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Appointment)
admin.site.register(LabTest)
admin.site.register(MedicineCategory)
admin.site.register(LabTestCategory)
admin.site.register(LabTestPrescription)
admin.site.register(MedicinePrescription)