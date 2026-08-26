from django.contrib import admin
from alpha_clinic.models import Doctor, Patient, Appointment, LabTest, Prescription, Medicine, MedicalRecord,Bill


# Register Doctor Model
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'email', 'phone', 'consultation_fees', 'created_at', 'updated_at')
    list_filter = ('specialization', 'consultation_fees')
    search_fields = ('name',)
admin.site.register(Doctor, DoctorAdmin)


# Register Patient Model
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'dob', 'email', 'address', 'blood_group', 'created_at', 'updated_at')
    list_filter = ('blood_group', 'gender')
    search_fields = ('name',)
admin.site.register(Patient, PatientAdmin)


# Register Appointment Model
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'remarks', 'status', 'created_at', 'updated_at','date_time')

admin.site.register(Appointment, AppointmentAdmin)


# Register LabTest Model
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

admin.site.register(LabTest, LabTestAdmin)



# Register Prescription Model
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'notes', 'created_at', 'updated_at')
    search_fields = ('notes',)

admin.site.register(Prescription, PrescriptionAdmin)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'strength', 'price', 'stock',)
    search_fields = ('medicine_name',)
admin.site.register(Medicine, MedicineAdmin)


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('diagnosis', 'allergies', 'medical_history', 'notes', 'created_at',)
    search_fields = ('diagnosis',)
admin.site.register(MedicalRecord, MedicalRecordAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ("id","discount","tax","grand_total","status","payment_date","created_at", "updated_at","appointment")
admin.site.register(Bill, BillAdmin)