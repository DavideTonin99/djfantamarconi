from django.conf import settings
from django.db import models

class Processes(models.Model):

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processi'

    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    start_date = models.DateField(auto_now=False, null=True, blank=True)
    end_date = models.DateField(auto_now=False, null=True, blank=True)
    referent = models.ForeignKey(settings.AUTH_USER_MODEL)
