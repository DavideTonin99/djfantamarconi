from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', lambda request: HttpResponseRedirect(reverse('fantamarconi:home'))),
	url(r'^', include('fantamarconi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^fantamarconi/', include('fantamarconi.urls'))
]
