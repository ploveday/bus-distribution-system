from django.db import models
from django.db.models import manager
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime, timedelta

#ticket table - pressed route data source
class Tickets(models.Model):
    ticketName = models.CharField(max_length=100)# Name of tickets
    route = models.CharField(max_length=200)# departure and destination route 
    #destination = models.CharField(max_length=100)# Proposed destination route 
    purchasedTime = models.DateTimeField(default=datetime.now()) #Time ticket was purchased
    status = models.CharField(max_length=100)# state of ticket -- sold = awaiting bus arival, available = unpurchased ticket, used = closed ticket
    busCapacity = models.IntegerField()

class AllRoutes(models.Model): #Available Routes used for generating Tickets
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(default=datetime.now()) 
    author = models.CharField(max_length=100) #created by
    status = models.CharField(max_length=100) #Active of inactive
    

class Buses(models.Model):
    busName = models.CharField(max_length=100)
    tDate = models.DateTimeField(default=datetime.now()) 
    status = models.CharField(max_length=100) #Loaded = passengers on board,  off=Not on duty, on = Awaiting deployment
