from rest_framework.routers import DefaultRouter

from .views import (
    AcademicYearViewSet,
    ClassSubjectViewSet,
    ClassViewSet,
    DepartmentViewSet,
    SchoolViewSet,
    SubjectViewSet,
    TimetableViewSet,
)

router = DefaultRouter()
router.register(r"schools", SchoolViewSet)
router.register(r"academic-years", AcademicYearViewSet)
router.register(r"departments", DepartmentViewSet)
router.register(r"classes", ClassViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"class-subjects", ClassSubjectViewSet)
router.register(r"timetables", TimetableViewSet)
urlpatterns = router.urls
