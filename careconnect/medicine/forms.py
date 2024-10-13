from django import forms
from medicine.models import Medicine

class AddMedicineForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Quantity',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    detail = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Detail',
            'class': 'w-full h-24 p-2 mb-4 border rounded',
        })
    )

    class Meta:
        model = Medicine
        fields = (
            "name",
            "quantity",
            "detail",
        )
