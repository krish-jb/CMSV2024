from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'medicineStock',views.MedicineStockViewSet)

urlpatterns = router.urls