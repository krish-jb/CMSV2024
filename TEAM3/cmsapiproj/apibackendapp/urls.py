
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'medicines',views.MedicineViewSets)
urlpatterns=router.urls