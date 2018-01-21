from django.conf import settings
from django.db import models
from django.urls import reverse

class Processes(models.Model):

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processi'

    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    start_date = models.DateField(auto_now=False, null=True, blank=True)
    end_date = models.DateField(auto_now=False, null=True, blank=True)
    referent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("modify-macroprocess", kwargs={"pk":self.id})

class Timeline(models.Model):

    class Meta:
        unique_together = (('process', 'referent', 'start_date'),)

    process = models.ForeignKey('Processes', on_delete=models.PROTECT)
    referent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    start_date = models.DateField(auto_now=False, null=True, blank=True)
    end_date = models.DateField(auto_now=False, null=True, blank=True)
    job = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return ", ".join([self.process.name, self.referent.username, self.job])

    def get_absolute_url(self):
        return reverse("modify-microprocess", kwargs={"pk":self.id})

class Organogram(models.Model):

    class Meta:
        verbose_name = 'Organigramma'
        verbose_name_plural = 'Organigramma'
        unique_together = (('name', 'surname', 'email', 'sector', 'role', 'parent_level'),)

    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    surname = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=255)
    sector = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    parent_level = models.ForeignKey('Organogram', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return ", ".join(['[ID:'+str(self.id), self.name, self.surname, 'PARENT:'+str(self.parent_level), ']'])
