from django.urls import path

from . import views

urlpatterns = [
    path('createSubject/', views.subjectCreation, name='subjectCreation'),
]
