from django.conf.urls import url
from django.views.generic import RedirectView, UpdateView
from fantamarconi.views import ( 
    home, organogram, get_organogram, timeline, get_timeline, ProcessesView, MyProcessesView,
    view_profile, edit_profile, register, get_user_info, help_view, change_password
)
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from .models import Processes, Timeline

# app_name = 'fantamarconi'

urlpatterns = [
    url(r'^profile/password/$', change_password, name='change_password'),
    url(r'^$', home, name='home'),
    # Organogram
    url(r'^organogram/$', organogram, name='organogram'),
    url(r'^ajax/get_organogram/$', get_organogram, name='get_organogram'),
    url(r'^organogram/add/$', RedirectView.as_view(url='/fantamarconi/admin/fantamarconi/organogram/add/'), name='add-organogram'),
    # Timeline
    url(r'^timeline/', timeline, name='timeline'),
    url(r'^timeline/(?P<referent>.+)/$', timeline, name='timeline'),
    url(r'^ajax/get_timeline/$', get_timeline, name='get_timeline'),
    url(r'^timeline/add/$', RedirectView.as_view(url='/fantamarconi/admin/fantamarconi/timeline/add/'), name='add-timeline'),
    # Processes
    url(r'^processes/$', ProcessesView.as_view(), name='processes'),
    url(r'^processes/add/$', RedirectView.as_view(url='/fantamarconi/admin/fantamarconi/processes/add/'), name='add-process'),
    url(r'^myprocesses/$', login_required(MyProcessesView.as_view()), name='myprocesses'),
    url(r'^myprocesses/(?P<pk>\d+)/$', login_required(UpdateView.as_view(
        model = Processes,
        fields = ['name','start_date', 'end_date','referent', 'technical_referent'],
        template_name = 'single_process.html',
        #redirect = 'MyProcessesView'
    )) , name="modify-macroprocess"),

    url(r'^myprocesses/micro/(?P<pk>\d+)/$', login_required(UpdateView.as_view(
        model = Timeline,
        fields = ['process','start_date', 'end_date','referent', 'job'],
        template_name = 'single_microprocess.html',
        #redirect = 'MyProcessesView'
    )) , name="modify-microprocess"),

    url(r'^login/$', login, kwargs={'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),  # Cambio template  di login
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^profile/$', view_profile, name='view-profile'),
    url(r'^profile/edit/$', edit_profile, name='edit-profile'),
    url(r'^register/$', register, name='register'),
    url(r'^ajax/get_user_info/$', get_user_info, name='get_user_info'),
    url(r'^help/$', help_view, name='help')
]
