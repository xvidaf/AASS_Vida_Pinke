from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class LogPredmet(models.Model):
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    nazov_triedy = models.CharField(max_length=255, null=True)