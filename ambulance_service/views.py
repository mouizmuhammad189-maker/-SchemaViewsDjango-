from django.shortcuts import render
from ambulance_service.models import Ambulance,EmergencyRequest

# Create your views here.
def list_ambulance(request):
    print("list appointments view is called...")

    ambulance = Ambulance.objects.all()

    context = {
        'ambulance': ambulance
    }

    return render(request, "ambulance_service/ambulance.html", context=context)



def list_emergency(request):
    print("list appointments view is called...")

    emergency = EmergencyRequest.objects.all()

    context = {
        'emergency': emergency
    }

    return render(request, "ambulance_service/emergency.html", context=context)

