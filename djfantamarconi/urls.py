from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import HttpResponseRedirect, reverse

urlpatterns = [
    url(r'^$', lambda request: HttpResponseRedirect(reverse('home'))),
	url(r'^', include('fantamarconi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^fantamarconi/', include('fantamarconi.urls'))
]
