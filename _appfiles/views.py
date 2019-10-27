from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect


#Template view Page for purchased tickets awaiting buses
def ticket(request):
    return render(request, "ticket.html")

#Defult home page
def index(request):
    return render(request, "index.html")


