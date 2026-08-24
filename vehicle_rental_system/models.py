from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=255),
    Cn = models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    driving_license_number = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Customer: {self.full_name}"

class Damages(models.Model):
    damage_date = models.DateField(auto_now_add=True)
    damage_type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    repair_cost = models.DecimalField(max_digits=8, decimal_places=2)
    customer_charge = models.DecimalField(max_digits=8, decimal_places=2)
    notes= models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"Damage: {self.damage_date}"

class Maintenance(models.Model):
    maintenance_date = models.DateField(auto_now_add=True)
    maintenance_type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    service_provider = models.CharField(max_length=255, blank=True, null=True)
    next_service_date = models.DateField(blank=True, null=True)
    status_choices=[
        ("Completed", "Completed"),
        ("Scheduled", "Scheduled"),
        ("In Progress", "In Progress"),

    ]
    status=models.CharField(max_length=255, choices=status_choices)
    notes= models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"Maintenance: {self.maintenance_date}"


class Rentals(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField(blank=True, null=True)
    actual_return_date = models.DateField(blank=True, null=True)
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=8, decimal_places=2)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_method= models.CharField(max_length=255, blank=True, null=True)
    status_choices=[
        ("Paid", "Paid"),
        ("Partially Paid", "Partially Paid"),
        ("Pending", "Pending"),
    ]
    payment_status=models.CharField(max_length=255, choices=status_choices)
    statuses_choices=[
        ("Completed", "Completed"),
        ("Active", "Active"),
        ("Cancelled", "Cancelled"),

    ]
    status=models.CharField(max_length=255, choices=status_choices)
    notes= models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"Rental: {self.rental_date}"

