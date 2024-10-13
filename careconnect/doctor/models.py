from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    class Gender(models.TextChoices):
        M = "M", "Male"
        F = "F", "Female"
        LGBT = "LGBT", "LGBT"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    hire_date = models.DateField()
    contact_number = models.CharField(max_length=100)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
