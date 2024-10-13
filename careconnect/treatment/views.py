from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import transaction

import json
from django.http import JsonResponse
from django.utils import timezone


from treatment.models import PatientMedicine, Appointment
from doctor.models import Doctor
from patient.models import Patient
from medicine.models import Medicine
from patient.forms import AddPatientForm
from treatment.forms import DateFilterForm

# Create your views here.

class TreatmentView(View):
    template_name = 'treatment.html'

    def get(self, request):
        patient = Patient.objects.all()
        form = AddPatientForm()

        context = {
            "patient": patient,
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddPatientForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('treatment')
        patient = Patient.objects.all()

        context = {
            "patient": patient,
            "form": form
        }
        return render(request, self.template_name, context)


class MedicinePatientView(View):
    template_name = 'medicine_patient.html'

    def get(self, request):
        medicine = Medicine.objects.all()
        form = AddPatientForm()

        context = {
            "medicine": medicine,
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        data = json.loads(request.body)
        patient_id = data.get('id')
        print(patient_id)

        # Do something with patient_id
        return JsonResponse({'patient_id': patient_id})

class MedicinePatientListView(View):
    template_name = 'medicine_patient_list.html'

    def get(self, request):
        medicine = Medicine.objects.all()
        form = AddPatientForm()

        context = {
            "medicine": medicine,
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # ดึงข้อมูลจาก POST
        medicine_id = request.POST.getlist('medicine_id[]')
        quantities = request.POST.getlist('quantity[]')
        doses = request.POST.getlist('dose[]')
        times = request.POST.getlist('time[]')
        details = request.POST.getlist('details[]')
        notifications = request.POST.getlist('notification[]')

        print(medicine_id)
        doctor = Doctor.objects.get(id=1)  # กำหนด doctor ที่เกี่ยวข้อง
        patient = Patient.objects.get(id=5)  # กำหนด patient ที่เกี่ยวข้อง

        # ลูปข้อมูลจากฟอร์มและบันทึกใน PatientMedicine model
        for i in range(len(medicine_id)):
            medicine = Medicine.objects.get(id=medicine_id[i])  # ดึง Medicine object ตามชื่อ

            # สร้าง PatientMedicine instance
            PatientMedicine.objects.create(
                doctor=doctor,
                patient=patient,
                medicine=medicine,
                quantity=quantities[i],
                take_per_dose=doses[i],
                time_to_take=times[i],
                detail=details[i] if details[i] else None,  # ถ้ามีรายละเอียด
                notification=notifications[i] == 'true'  # แปลงเป็น Boolean
            )

        notification = request.POST.get('appointment_notification')
        print("Notification: ", notification)
        if notification == 'true':
            notification_value = True
        else:
            notification_value = False

        print(notification_value)

        if notification_value:
            appointment_date = request.POST.get('date')
            appointment_time = request.POST.get('time')
            detail = request.POST.get('detail')

            # ดึงข้อมูล Doctor และ Patient จาก database
            doctor = Doctor.objects.get(id=1)
            patient = Patient.objects.get(id=5)

            # สร้าง Appointment instance
            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                date=appointment_date,
                time=appointment_time,
                detail=detail
            )

        return redirect('treatment')


class AppointmentView(View):
    template_name = 'appointment.html'
    def get(self, request):
        today = timezone.now().date()

        form = DateFilterForm(request.GET or {'date': today})
        print(form)

        appointments = Appointment.objects.all()

        if form.is_valid():
            selected_date = form.cleaned_data.get('date')
            if selected_date:
                appointments = appointments.filter(date=selected_date)

                for i in appointments:
                    print(i.id)

        context = {
            "appointments": appointments,
            "form": form
        }
        return render(request, self.template_name, context)

