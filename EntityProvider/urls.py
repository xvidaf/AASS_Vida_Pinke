from django.urls import path

from EntityDisplay.views import zobrazZoznamPredmetovRest
from EntityManagement.views import subjectCreationRest

urlpatterns = [
    path('hours', zobrazZoznamPredmetovRest),
]
