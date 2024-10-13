from django import forms
from doctor.models import Doctor
from django.contrib.auth.models import User
from datetime import date

class AddDoctorForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    last_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    gender = forms.ChoiceField(
        choices=Doctor.Gender.choices,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-2 mb-4 border rounded'
        }),
        required=True
    )

    contact_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Contact Number',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    class Meta:
        model = Doctor
        fields = (
            "first_name",
            "last_name",
            "gender",
            "hire_date",
            "contact_number",
        )

    def save(self, commit=True):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username=username, password=password)

        doctor = super().save(commit=False)
        doctor.account = user

        if commit:
            doctor.save()
        return doctor

    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')
        if hire_date and hire_date > date.today():
            raise forms.ValidationError("Please enter a valid hire date that is not in the future.")
        return hire_date

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number should contain only digits.")
        if len(contact_number) < 10:
            raise forms.ValidationError("Contact number must be at least 10 digits.")
        return contact_number
