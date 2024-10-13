from django.urls import path

from patient.views import PatientMedicineView

urlpatterns = [
    path('', PatientMedicineView.as_view(), name="patient-medicine"),
    path('medicine/<int:year>/<int:month>/', PatientMedicineView.as_view(), name='patient-medicine-calendar'),
]
