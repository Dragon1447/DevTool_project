from django.urls import path

from medicine.views import MedicineView, UpdateMedicineView, DeleteMedicineView

urlpatterns = [
    path('', MedicineView.as_view(), name="medicine"),
    path('update/<int:id>/', UpdateMedicineView.as_view(), name="update-medicine"),
    path('delete/<int:id>/', DeleteMedicineView.as_view(), name="delete-medicine"),
]
