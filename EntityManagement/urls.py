from django.urls import path, include
from rest_framework import routers
from . import views
from .views import subjectCreationRest

urlpatterns = [
    path('createSubject/', views.subjectCreation, name='subjectCreation'),
    path('createSubjectRest', subjectCreationRest),
]
