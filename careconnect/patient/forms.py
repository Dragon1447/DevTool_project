from django import forms
from patient.models import Patient
from django.contrib.auth.models import User

class AddPatientForm(forms.ModelForm):
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

    id_number = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={
            'placeholder': 'ID Number',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    gender = forms.ChoiceField(
        choices=Patient.Gender.choices,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    contact_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Contact Number',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    status = forms.ChoiceField(
        choices=Patient.StatusPatient.choices,
        widget=forms.Select(attrs={
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
        model = Patient
        fields = (
            "first_name",
            "last_name",
            "id_number",
            "gender",
            "contact_number",
            "status",
        )

    def save(self, commit=True):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username=username, password=password)

        patient = super().save(commit=False)
        patient.account = user

        if commit:
            patient.save()
        return patient

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number should contain only digits.")
        if len(contact_number) < 10:
            raise forms.ValidationError("Contact number must be at least 10 digits.")
        return contact_number

    def clean_id_number(self):
        id_number = self.cleaned_data.get('id_number')
        if not id_number.isdigit():
            raise forms.ValidationError("ID number should contain only digits.")
        if len(id_number) < 13:
            raise forms.ValidationError("ID number must be at least 13 digits.")
        return id_number
