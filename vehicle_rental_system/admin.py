from django.contrib import admin
from vehicle_rental_system.models import *

#adding models
@ admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","Cn","phone","email_address","driving_license_number","created_at","updated_at")
    search_fields = ("Full_name","Cn","Phone","Email_Address")
    list_filter = ("driving_license_number","Cn")

@ admin.register(Damages)
class DamagesAdmin(admin.ModelAdmin):
    list_display = ("id","damage_date","damage_type","description","repair_cost","customer_charge","notes","created_at", "updated_at")
    search_fields = ("damage_date",)
    list_filter = ("damage_date","damage_type","repair_cost")

@ admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("id","maintenance_date","maintenance_type","description","cost","service_provider","created_at", "updated_at","next_service_date","notes","status")
    search_fields = ("maintenance_date","maintenance_type")
    list_filter = ("maintenance_date","maintenance_type","cost")

@ admin.register(Rentals)
class RentalsAdmin(admin.ModelAdmin):
    list_display = ("id","rentals_date","expected_return_date","actual_return_date","daily_rate","security_deposit","total_amount","payment_amount","payment_method","payment_status","status","notes","created_at", "updated_at")
    search_fields = ("expected_return_date","actual_return_date","rentals_date")
    list_filter = ("daily_rate","payment_methode")





# Register your models here.


