from django.urls import path

from treatment.views import TreatmentView, MedicinePatientView, MedicinePatientListView, AppointmentView

urlpatterns = [
    path('', TreatmentView.as_view(), name="treatment"),
    path('medicine/', MedicinePatientView.as_view(), name="medicine-patient"),
    path('medicine/list/', MedicinePatientListView.as_view(), name="medicine-patient-list"),
    path('appointment', AppointmentView.as_view(), name="appointment"),
]
