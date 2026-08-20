from django.db import models
from pyexpat import model


# Create your models here.
class Ambulance(models.Model):
    vehicle_number = models.CharField(max_length=255, unique=True)
    driver_name= models.CharField(max_length=255)
    ambulance_type = models.CharField(max_length=255)
    vehicle_status_choices=[
        ("A","Available"),
        ("B","Busy"),
        ("M","Maintenance"),
    ]
    ambulance_status = models.CharField(max_length=255, choices=vehicle_status_choices)

    def __str__(self):
        return f"Vehicle {self.vehicle_number}"

class EmergencyRequest(models.Model):
    patient_name=models.CharField(max_length=255)
    priority_choices=[
        ("A","Low"),
        ("B","Medium"),
        ("C","High"),
    ]
    priority_status = models.CharField(max_length=255, choices=priority_choices)
    request_time = models.DateTimeField(auto_now_add=True)
    status_choices=[
        ("A","Pending"),
        ("B","Dispatch"),
        ("C","Completed"),
    ]
    status_status = models.CharField(max_length=255, choices=status_choices)
    ambulance_id=models.ForeignKey(Ambulance, on_delete=models.CASCADE)