from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    class Gender(models.TextChoices):
        M = "M", "Male"
        F = "F", "Female"
        LGBT = "LGBT", "LGBT"

    class StatusPatient(models.TextChoices):
        I = "I", "Independent Elderly"          # ผู้ป่วยชราที่พึ่งพาตนเองได้
        P = "P", "Partially Dependent Elderly"  # ผู้ป่วยชราที่ต้องการความช่วยเหลือบางส่วน
        F = "F", "Fully Dependent Elderly"      # ผู้ป่วยชราที่ต้องการความช่วยเหลือตลอดเวลา
        B = "B", "Bedridden Elderly"            # ผู้ป่วยชราที่นอนติดเตียง
        D = "D", "Dementia Elderly"             # ผู้ป่วยชราที่มีภาวะสมองเสื่อม

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=14)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    contact_number = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=StatusPatient.choices)
    account = models.OneToOneField(User, on_delete=models.CASCADE)
