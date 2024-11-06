from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r"prescriptions", views.MedicineCategoryViewSet)

urlpatterns = router.urls
