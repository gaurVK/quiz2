from rest_framework import routers
from .views import EmployeeViewSet, AttendanceViewSet, PerformanceViewSet, SalaryHistoryViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)
router.register(r'salary', SalaryHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
