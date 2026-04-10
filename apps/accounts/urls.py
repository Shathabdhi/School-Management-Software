from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ParentViewSet,
    RequestOTPView,
    StudentViewSet,
    TeacherViewSet,
    UserViewSet,
    VerifyOTPView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"students", StudentViewSet)
router.register(r"parents", ParentViewSet)
urlpatterns = router.urls + [
    path("auth/request-otp/", RequestOTPView.as_view()),
    path("auth/verify-otp/", VerifyOTPView.as_view()),
]
