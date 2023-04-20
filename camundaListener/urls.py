from django.contrib import admin
from django.urls import path

from camundaListener import views

urlpatterns = [
    path('camunda',views.camundaProces,name="camundaProces"),
    ]


