from rest_framework.routers import DefaultRouter

from .views import FeePaymentViewSet, FeeStructureViewSet

router = DefaultRouter()
router.register(r"fee-structures", FeeStructureViewSet)
router.register(r"fee-payments", FeePaymentViewSet)
urlpatterns = router.urls
