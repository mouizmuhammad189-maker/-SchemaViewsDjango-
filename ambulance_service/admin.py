from django.contrib import admin
from ambulance_service.models import *
# Register your models here.

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ("id","vehicle_number","driver_name","ambulance_type","ambulance_status",)
    search_fields = ("vehicle_number",)
    list_filter = ("ambulance_type","ambulance_status","driver_name")

admin.site.register(Ambulance,AmbulanceAdmin)



@admin.register(EmergencyRequest)
class EmergencyRequestAdmin(admin.ModelAdmin):
    list_display = ("id","patient_name","priority_status","request_time","request_status","ambulance_id")
    search_fields = ("patient_name",)
    list_filter = ("ambulance_id","request_time","request_status",)
