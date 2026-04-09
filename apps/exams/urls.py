from rest_framework.routers import DefaultRouter

from .views import ExamResultViewSet, ExamScheduleViewSet, ExamViewSet

router = DefaultRouter()
router.register(r"exam-results", ExamResultViewSet)
router.register(r"exam-schedules", ExamScheduleViewSet)
router.register(r"exams", ExamViewSet)
urlpatterns = router.urls
