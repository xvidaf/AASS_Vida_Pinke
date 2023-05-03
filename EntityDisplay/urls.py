"""AASS_Vida_Pinke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from EntityDisplay import views

urlpatterns = [
    path('', views.zobrazZoznamPredmetov, name="zobrazZoznamPredmetov"),
    path('hour/<predmet_id>', views.hour, name="hour"),
    path('zobrazPredmet/<int:lesson_id>', views.zobrazPredmetRest, name="zobrazPredmet"),
    path('zobrazZoznamPredmetov', views.zobrazZoznamPredmetovRest, name="zobrazZoznamPredmetovRest"),
    #path('teacher', views.teacher_list, name="teacher_list"),
    #path('lesson', views.lesson_list, name="lesson_list"),
]
