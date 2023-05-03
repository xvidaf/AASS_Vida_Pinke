from django.urls import path

from . import views
from .views import subjectCreationRest

urlpatterns = [
    path('createSubject/', views.subjectCreation, name='subjectCreation'),
]
