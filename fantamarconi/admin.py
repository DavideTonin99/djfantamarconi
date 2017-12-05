from django.contrib import admin

from .models import Processes, Timeline, Organogram

# Register your models here.
admin.site.register(Processes)
admin.site.register(Timeline)
admin.site.register(Organogram)
