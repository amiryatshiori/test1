from django.db import models
from company.models import Company

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    