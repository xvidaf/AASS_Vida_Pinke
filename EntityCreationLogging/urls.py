from django.urls import path

from . import views

urlpatterns = [
    path('writeToLog/', views.writeToLog, name='writeToLog'),
    path('log', views.writeToLogRest),
]
