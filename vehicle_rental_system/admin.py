from django.contrib import admin
from vehicle_rental_system.models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "Cn",
        "phone",
        "email_address",
        "driving_license_number",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "full_name",
        "Cn",
        "phone",
        "email_address",
    )

    list_filter = (
        "driving_license_number",
        "Cn",
    )


@admin.register(Damages)
class DamagesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "damage_date",
        "damage_type",
        "description",
        "repair_cost",
        "customer_charge",
        "notes",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "damage_type",
        "description",
    )

    list_filter = (
        "damage_date",
        "damage_type",
        "repair_cost",
    )


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "maintenance_date",
        "maintenance_type",
        "description",
        "cost",
        "service_provider",
        "created_at",
        "updated_at",
        "next_service_date",
        "notes",
        "status",
    )

    search_fields = (
        "maintenance_type",
        "description",
        "service_provider",
    )

    list_filter = (
        "maintenance_date",
        "maintenance_type",
        "cost",
        "status",
    )


@admin.register(Rentals)
class RentalsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "rental_date",
        "expected_return_date",
        "actual_return_date",
        "daily_rate",
        "security_deposit",
        "total_amount",
        "payment_amount",
        "payment_method",
        "payment_status",
        "status",
        "notes",
        "created_at",
        "updated_at",
        "customer",
        "vehicle",
    )

    search_fields = (
        "expected_return_date",
        "actual_return_date",
        "rental_date",
        "customer__full_name",
        "vehicle__registration_no",
    )

    list_filter = (
        "daily_rate",
        "payment_method",
        "payment_status",
        "status",
    )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "registration_no",
        "vehicle_type",
        "brand",
        "model",
        "manufacturing_year",
        "color",
        "daily_rate",
        "mileage",
        "status",
        "purchase_date",
    )

    search_fields = (
        "registration_no",
        "vehicle_type",
        "brand",
        "model",
    )

    list_filter = (
        "vehicle_type",
        "brand",
        "model",
        "status",
    )