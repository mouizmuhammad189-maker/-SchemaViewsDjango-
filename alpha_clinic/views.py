from django.shortcuts import render
from alpha_clinic.models import *

# Create your views here.
"""
Doctor Patient LabTest  Appointment   Prescription   Medicine   MedicalRecord   Bill"""


def list_doctor(request):
    doctors = Doctor.objects.all()
    context = {'doctors':doctors}
    return render(request, "alpha_clinic/doctors.html", context)


def list_patient(request):
    patient = Patient.objects.all()
    context = {'patient':patient}
    return render(request, "alpha_clinic/patients.html", context)



def list_labtest(request):
    labtest = LabTest.objects.all()
    context = {'labtest':labtest}
    return render(request, "alpha_clinic/Lab tests.html", context)


def list_appointment(request):
    appointment = Appointment.objects.all()
    context = {'appointment':appointment}
    return render(request, "alpha_clinic/appointments.html", context)


def list_prescription(request):
    prescription = Prescription.objects.all()
    context = {'prescriptions':prescription}
    return render(request, "alpha_clinic/prescriptions.html", context)


def list_medicine(request):
    medicine = Medicine.objects.all()
    context = {'medicines':medicine}
    return render(request, "alpha_clinic/medicines.html", context)

def list_medical_record(request):
    medical_record = MedicalRecord.objects.all()
    context = {'medical_records':medical_record}
    return render(request, "alpha_clinic/medical_records.html", context)


def list_bill(request):
    bill = Bill.objects.all()
    context = {'bills':bill}
    return render(request, "alpha_clinic/bills.html", context)


