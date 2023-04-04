from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class Ucitel(models.Model):
    bydlisko = models.CharField(max_length=255, null=True)
    meno = models.CharField(max_length=255, null=True)
    priezvisko = models.CharField(max_length=255, null=True)
    rodneCislo = models.CharField(max_length=255, null=True)
    jeMuz = models.BooleanField(null=True)

    def __str__(self):
        if self.priezvisko:
            return self.priezvisko
        else:
            return "NOT FOUND"

class Trieda(models.Model):
    class Rocnik(models.TextChoices):
        prvy = '1', _('Prvy rocnik')
        druhy = '2', _('Druhy rocnik')
        treti = '3', _('Treti rocnik')
        stvrty = '4', _('Stvrty rocnik')
        piaty = '5', _('Piaty rocnik')
        siesty = '6', _('Siesty rocnik')
        siedmy = '7', _('Siedmy rocnik')
        osmi = '8', _('Osmi rocnik')
        deviaty = '9', _('Deviaty rocnik')

    rocnik = models.CharField(
        max_length=1,
        choices=Rocnik.choices,
        default=Rocnik.prvy,
    )
    nazov = models.CharField(max_length=255, null=True)
    ucitel = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.nazov:
            return self.nazov
        else:
            return "NOT FOUND"

"""
class Predmet(models.Model):
    detaily = models.CharField(max_length=255, null=True)
    nazov = models.CharField(max_length=255, null=True)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)

class Student(models.Model):
    bydlisko = models.CharField(max_length=255, null=True)
    meno = models.CharField(max_length=255, null=True)
    priezvisko = models.CharField(max_length=255, null=True)
    rodneCislo = models.CharField(max_length=255, null=True)
    pohlavie = models.BooleanField()
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)

class PredmetToTrieda(models.Model):
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    predmet = models.ForeignKey(Predmet, on_delete=models.SET_NULL, null=True, blank=True)

class Hodina(models.Model):
    predmet = models.ForeignKey(Predmet, on_delete=models.SET_NULL, null=True, blank=True)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    ucitel = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True, blank=True)
    cas = models.TimeField(null=True)
    def __str__(self):
        if self.predmet:
            return self.predmet
        else:
            return "NOT FOUND"
class LogPredmet(models.Model):
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    nazov_triedy = models.CharField(max_length=255, null=True)
"""