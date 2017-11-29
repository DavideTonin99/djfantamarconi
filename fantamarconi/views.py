from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from fantamarconi.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm

from fantamarconi.models import Processes

def home(request):
    return render(request, template_name='home.html')

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

def view_profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'register.html', args)
