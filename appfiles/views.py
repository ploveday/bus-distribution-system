from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models as tModel

#function that checks for ticket purchase activities at all routes
def butActivities(today):
    highBuy = tModel.Tickets.objects.filter(status='sold').filter(purchasedTime <= today)
    qtySold = highBuy.count()
    routeToAssign = {
        'route': highBuy.route,
        'qtySold': qtySold,
        'busCapacity':highBuy.busCapacity
        }
    return routeToAssign

# Gets denslly populated route. Returns 
def assignRoute(location):
    from math import ceil
    busCapacity = 20
    for key, value in location.items():
        deploy = ceil(value / busCapacity)
        location[key] = deploy
    deploying = location
    return deploying

#Template view Page for purchased tickets awaiting buses
def ticket(request):
    return render(request, "ticket.html")

#Defult home page
def index(request):
    return render(request, "index.html")


