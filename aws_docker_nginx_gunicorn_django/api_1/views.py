from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee


# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
