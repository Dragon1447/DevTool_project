from django.db import models
from doctor.models import Doctor
from patient.models import Patient
from medicine.models import Medicine

# Create your models here.
class Treatment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PatientMedicine(models.Model):
    class TimeToTake(models.TextChoices):
        AC_TID = "AC_TID", "Ante Cibum Three Times a Day"   # เช้า กลางวัน เย็น (ก่อนกินข้าว)
        PC_TID = "PC TID", "Post Cibum Three Times a Day"   # เช้า กลางวัน เย็น (หลังกินข้าว)
        AC_BID = "AC BID", "Ante Cibum Twice a Day"         # เช้า เย็น (ก่อนกินข้าว)
        PC_BID = "PC BID", "Post Cibum Twice a Day"         # เช้า เย็น (หลังกินข้าว)
        AC_Noon = "AC Noon", "Ante Cibum at Noon"           # กลางวัน (ก่อนกินข้าว)
        PC_Noon = "PC Noon", "Post Cibum at Noon"           # กลางวัน (หลังกินข้าว)
        HS = "HS", "Hora Somni"                             # ก่อนนอน

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    take_per_dose = models.IntegerField()
    time_to_take = models.CharField(
        max_length=10,
        choices=TimeToTake.choices,
        default=TimeToTake.AC_TID  # Set a default value if desired
    )
    detail = models.TextField(null=True, blank=True)
    notification = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
