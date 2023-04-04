from django.db import models
from django.utils.translation import gettext_lazy as _

from EntityProvider.models import Trieda


class Predmet(models.Model):
    detaily = models.CharField(max_length=255, null=True)
    nazov = models.CharField(max_length=255, null=True)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
