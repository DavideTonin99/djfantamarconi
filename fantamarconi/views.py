from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from fantamarconi.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from fantamarconi.models import Processes

def home(request):
    return render(request, template_name='home.html')

def timeline(request):
    return render(request, template_name='timeline.html')

def get_timeline(request):
    return JsonResponse({'ciao':'ciao'})

class ProcessesView(TemplateView):

    model = Processes
    template_name = 'processes.html'

    def get_context_data(self, **kwargs):
        context = super(ProcessesView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the processes
        processes = Processes.objects.all()

        context['processes'] = [({'process':process,
                                'referent_name': process.referent.first_name,
                                'referent_surname': process.referent.last_name,
                                'referent_email': process.referent.email})
                                for process in processes]
        return context

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
            form = RegistrationForm()
            args = {'form':form}
            return render(request, 'register.html', args)
