from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import transaction

import json
from django.http import JsonResponse

from doctor.models import Doctor
from doctor.forms import AddDoctorForm



# Create your views here.

class DoctorView(View):
    template_name = "doctor.html"
    def get(self, request):
        doctor = Doctor.objects.all()

        form = AddDoctorForm()

        context = {
            "doctor": doctor,
            "form": form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = AddDoctorForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('doctor')
        doctor = Doctor.objects.all()

        context = {
            "doctor": doctor,
            "form": form
        }
        return render(request, self.template_name, context)


class UpdateDoctorView(View):
    def put(self, request, id):
        try:
            # รับข้อมูลฟอร์มและอัปเดตข้อมูลหมอ
            data = json.loads(request.body)
            doctor = Doctor.objects.get(id=id)
            doctor.first_name = data.get('first_name')
            doctor.last_name = data.get('last_name')
            doctor.contact_number = data.get('contact_number')
            doctor.save()

            return redirect('doctor')
        except Doctor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'ไม่พบข้อมูลหมอ!'}, status=404)



class DeleteDoctorView(View):
    def delete(self, request, id):
        try:
            doctor = Doctor.objects.get(id=id)
            doctor.delete()
            return redirect('doctor')
        except Doctor.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Doctor not found!'}, status=404)
