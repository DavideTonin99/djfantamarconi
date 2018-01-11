from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from fantamarconi.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from fantamarconi.models import Processes, Timeline, Organogram

def home(request):
    return render(request, template_name='home.html')


class ProcessesView(TemplateView):

    model = Processes
    template_name = 'processes.html'

    def get_context_data(self, **kwargs):
        context = super(ProcessesView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the processes
        processes = Processes.objects.all()

        if (len(processes) > 0):
            context['processes'] = [({'process':process,
                                    'referent_name': process.referent.first_name,
                                    'referent_surname': process.referent.last_name,
                                    'referent_email': process.referent.email})
                                    for process in processes]
        else:
            context['macro_processes_error'] = 'Nessun risultato trovato'
        return context


class MyProcessesView(TemplateView):
    model = Processes
    template_name = 'processes.html'

    def get_context_data(self, **kwargs):
        context = super(MyProcessesView, self).get_context_data(**kwargs)

        if (self.request.user.is_superuser):
            macro_processes = Processes.objects.all()
            timeline_processes = Timeline.objects.all()
        else:
            macro_processes = Processes.objects.all().filter(referent = self.request.user)
            timeline_processes = Timeline.objects.all().filter(referent = self.request.user)

        context['page'] = "myprocesses"

        if (len(macro_processes) > 0):
            context['processes'] = [({'process':process,
                                    'referent_name': process.referent.first_name,
                                    'referent_surname': process.referent.last_name,
                                    'referent_email': process.referent.email})
                                    for process in macro_processes]
        else:
            context['macro_processes_error'] = 'Nessun Macro Processo trovato'

        if (len(timeline_processes) > 0):
            context['timeline_processes'] = [({'process':process,
                                    'referent_name': process.referent.first_name,
                                    'referent_surname': process.referent.last_name,
                                    'referent_email': process.referent.email})
                                    for process in timeline_processes]
        else:
            context['timeline_processes_error'] = 'Nessun processo trovato'

        return context

# organogram page
def organogram(request):
    return render(request, template_name='organogram.html')

# return organogram data
def get_organogram(request):
    organogram = {}
    objects = Organogram.objects.all()

    if (len(objects) > 0):
        for obj in objects:
            if obj.parent_level == None:
                parent_level = obj.id
            else:
                parent_level = obj.parent_level.id

            organogram[obj.id] = {
                            'id': obj.id,
                            'name': obj.name,
                            'surname': obj.surname,
                            'email': obj.email,
                            'sector': obj.sector,
                            'role': obj.role,
                            'parent_level': parent_level
                            }

    else:
        organogram['error'] = "Nessun dato trovato. Riprovare o contattare l'amministratore."

    return JsonResponse(organogram)

# timeline page
def timeline(request):
    return render(request, template_name='timeline.html')

# return timeline data
def get_timeline(request):
    timeline = {}

    first_name = request.GET['first_name']
    last_name = request.GET['last_name']

    # check for referent selection
    if (first_name != "" or last_name != ""):
        processes = Timeline.objects.filter(referent__first_name__contains=first_name, referent__last_name__contains=last_name)
    else:
        processes = Timeline.objects.all()

    if (len(processes) > 0):
        id = 0
        for record in processes:
            timeline[id] = {
                            'processo': record.process.name,
                            'referente': record.referent.first_name +' '+ record.referent.last_name,
                            'data_inizio': record.start_date,
                            'data_fine': record.end_date,
                            'compito': record.job
                            }
            id += 1
    else:
        timeline['error'] = "Nessun dato trovato. Riprovare o contattare l'amministratore."

    return JsonResponse(timeline)


@login_required
def view_profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view-profile')
        else:
            args = {'form':form}
            return render(request, 'edit_profile.html', args)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'edit_profile.html', args)


@login_required
def register(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                args = {'form':form}
                return render(request, 'register.html', args)
        else:
            form = RegistrationForm()
            args = {'form':form}
            return render(request, 'register.html', args)
