from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()
router.register(r'doctors',views.DoctorViewSet)
urlpatterns = router.urls
