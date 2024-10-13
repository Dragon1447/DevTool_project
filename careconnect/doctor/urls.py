from django.urls import path

from doctor.views import DoctorView, UpdateDoctorView, DeleteDoctorView

urlpatterns = [
    path('', DoctorView.as_view(), name="doctor"),
    path('update/<int:id>/', UpdateDoctorView.as_view(), name="update-doctor"),
    path('delete/<int:id>/', DeleteDoctorView.as_view(), name="delete-doctor"),
]
