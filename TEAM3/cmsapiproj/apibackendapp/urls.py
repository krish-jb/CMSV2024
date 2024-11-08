from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register(r'doctors',views.DoctorViewSet)
router.register(r"prescriptions/medicine", views.MedicinePrescriptionViewSet)
router.register(r"prescriptions/labtest", views.LabTestPrescriptionViewSet)
router.register(r'medicineStock',views.MedicineStockViewSet)
router.register(r'medicines',views.MedicineViewSets)

urlpatterns = router.urls