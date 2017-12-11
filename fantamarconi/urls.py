from django.conf.urls import url
from django.views.generic import RedirectView, UpdateView
from fantamarconi.views import ( home, organogram, get_organogram,
                                timeline, get_timeline, ProcessesView, MyProcessesView,
                                view_profile, edit_profile, register )
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from .models import Processes

# app_name = 'fantamarconi'

urlpatterns = [
    url(r'^$', home, name='home'),
    # Organogram
    url(r'^organogram/$', organogram, name='organogram'),
    url(r'^ajax/get_organogram/$', get_organogram, name='get_organogram'),
    url(r'^organogram/add/$', RedirectView.as_view(url='/admin/fantamarconi/organogram/add/'), name='add-organogram'),
    # Timeline
    url(r'^timeline/$', timeline, name='timeline'),
    url(r'^ajax/get_timeline/$', get_timeline, name='get_timeline'),
    url(r'^timeline/add/$', RedirectView.as_view(url='/admin/fantamarconi/timeline/add/'), name='add-timeline'),
    # Processes
    url(r'^processes/$', ProcessesView.as_view(), name='processes'),
    url(r'^processes/add/$', RedirectView.as_view(url='/admin/fantamarconi/processes/add/'), name='add-process'),
    url(r'^myprocesses/$', login_required(MyProcessesView.as_view()), name='myprocesses'),
    url(r'^myprocesses/(?P<slug>[\w-]+)/$', login_required(UpdateView.as_view(
        model = Processes,
        fields = ['name','start_date', 'end_date','referent'],
        template_name = 'single_process.html',
        #redirect = 'MyProcessesView'
    )) , name="processo"),

    url(r'^login/$', login, kwargs={'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),  # Cambio template  di login
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^profile/$', view_profile, name='view-profile'),
    url(r'^profile/edit/$', edit_profile, name='edit-profile'),
    url(r'^register/$', register, name='register')
]
