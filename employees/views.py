from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Employee, Attendance, Performance, SalaryHistory
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceSerializer, SalaryHistorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import pandas as pd
from django.http import HttpResponse

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False)
    def export_csv(self, request):
        qs = self.get_queryset()
        df = pd.DataFrame(list(qs.values()))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'
        df.to_csv(path_or_buf=response, index=False)
        return response

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class SalaryHistoryViewSet(viewsets.ModelViewSet):
    queryset = SalaryHistory.objects.all()
    serializer_class = SalaryHistorySerializer
