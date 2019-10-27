from django.urls import path
from . import views

urlpatterns = [
    path('ticket', views.ticket, name="ticket"),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
]