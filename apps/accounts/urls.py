from rest_framework.routers import DefaultRouter

from .views import ParentViewSet, StudentViewSet, TeacherViewSet, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"students", StudentViewSet)
router.register(r"parents", ParentViewSet)
urlpatterns = router.urls
