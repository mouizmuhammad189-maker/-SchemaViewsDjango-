from django.urls import path
from ambulance_service import views


urlpatterns = [
    path('ambulances/', views.list_ambulance, name="list_ambulance"),
    path('emergency/', views.list_emergency, name="list_emergency"),
]