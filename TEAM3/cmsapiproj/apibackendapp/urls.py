from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r"prescriptions/medicine", views.MedicinePrescriptionViewSet)

router.register(r"prescriptions/labtest", views.LabTestPrescriptionViewSet)

urlpatterns = router.urls
