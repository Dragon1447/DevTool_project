from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import transaction

import json
from django.http import JsonResponse

from medicine.models import Medicine
from medicine.forms import AddMedicineForm

# Create your views here.

class MedicineView(View):
    template_name = 'medicine.html'

    def get(self, request):
        medicine = Medicine.objects.all()
        form = AddMedicineForm()

        context = {
            "medicine": medicine,
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddMedicineForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('medicine')
        medicine = Medicine.objects.all()

        context = {
            "medicine": medicine,
            "form": form
        }
        return render(request, self.template_name, context)

class UpdateMedicineView(View):
    def put(self, request, id):
        try:
            # รับข้อมูลฟอร์มและอัปเดตข้อมูลหมอ
            data = json.loads(request.body)
            medicine = Medicine.objects.get(id=id)
            medicine.name = data.get('name')
            medicine.quantity = data.get('quantity')
            medicine.detail = data.get('detail')
            medicine.save()

            return redirect('medicine')
        except Medicine.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'ไม่พบข้อมูลหมอ!'}, status=404)



class DeleteMedicineView(View):
    def delete(self, request, id):
        try:
            medicine = Medicine.objects.get(id=id)
            medicine.delete()
            return redirect('medicine')
        except Medicine.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'medicine not found!'}, status=404)

