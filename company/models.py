from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=13)
    