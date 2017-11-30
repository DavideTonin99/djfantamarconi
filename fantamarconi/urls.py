from django.conf.urls import url
from fantamarconi.views import home, timeline, get_timeline, ProcessesView, view_profile, edit_profile, register
from django.contrib.auth.views import login, logout

# app_name = 'fantamarconi'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^timeline/$', timeline, name='timeline'),
    url(r'^ajax/get_timeline/$', get_timeline, name='get_timeline'),
    url(r'^processes/$', ProcessesView.as_view(), name='processes'),
    url(r'^login/$', login, kwargs={'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),  # Cambio template  di login
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^profile/$', view_profile, name='view-profile'),
    url(r'^profile/edit/$', edit_profile, name='edit-profile'),
    url(r'^register/$', register, name='register')
]
