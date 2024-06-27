from django.db import models
import uuid


# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    description4 = models.TextField(blank=True, null=True)
    description5 = models.TextField(blank=True, null=True)
    description6 = models.TextField(blank=True, null=True)
    description7 = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    company = models.ForeignKey(
        Company,
        related_name="employees",
        on_delete=models.CASCADE,
    )
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + str(self.company)
