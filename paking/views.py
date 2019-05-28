from django.shortcuts import render
from .models import *

# Create your views here.



def slot_card(request):
    carplate = ""
    type = ""
    color = ""
    car = Car.objects.filter(carplate=carplate, type=type, color=color)
    time = car[0].out_time - car[0].in_time
    pass