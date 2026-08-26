from django.urls import path
from alpha_clinic import views
"""
Doctor Patient LabTest  Appointment   Prescription   Medicine   MedicalRecord   Bill"""
urlpatterns = [
    path('patient/', views.list_patient, name="patient"),
    path('doctor/', views.list_doctor, name="doctor"),
    path('labtest/', views.list_labtest, name="labtest"),
    path('medicine/', views.list_medicine, name="medicine"),
    path('appointment/', views.list_appointment, name="appointment"),
    path('prescription/', views.list_prescription, name="prescription"),
    path('medical_record/', views.list_medical_record, name="medicine"),
    path('Bill/', views.list_bill, name="bill"),
]