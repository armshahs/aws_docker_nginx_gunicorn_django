from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "location",
            "description",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            "id",
            "name",
            "email",
            "phone",
            "about",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
