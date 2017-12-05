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

    def __str__(self):
        return str(self.name)


class Timeline(models.Model):

    class Meta:
        unique_together = (('process', 'referent', 'start_date'),)

    process = models.ForeignKey('Processes')
    referent = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_date = models.DateField(auto_now=False, null=True, blank=True)
    end_date = models.DateField(auto_now=False, null=True, blank=True)
    job = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return ", ".join([self.process.name, self.referent.username, self.job])

class Organogram(models.Model):

    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    surname = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=255)
    sector = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    parent_level = models.IntegerField()

    def __str__(self):
        return ", ".join([self.name, self.surname, str(self.parent_level)])
