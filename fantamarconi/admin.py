from django.contrib import admin

from .models import Processes, Timeline, Organogram

#class ProcessesAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('name',)}

#    class Meta:
#        model = Processes

# Register your models here.
#admin.site.register(Processes, ProcessesAdmin)
admin.site.register(Processes)
admin.site.register(Timeline)
admin.site.register(Organogram)
