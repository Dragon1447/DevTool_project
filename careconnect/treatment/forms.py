from django import forms
from django.forms import ModelForm, DateInput
from treatment.models import Appointment
from datetime import date
from django.utils import timezone

class DateFilterForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'value': timezone.now().date(),
                }
            ),
        }
