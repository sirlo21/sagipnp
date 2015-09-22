from django.conf.urls import patterns, include, url
from django.contrib import admin
from sagi_pnp import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("levantamiento.urls")),
    url(r'^ayudas/', include("ayudas.urls")),
    url(r'^ubigeo/', include('ubigeo.urls')),
    url(r'^', include('metrados.urls')),
	# url(r'^users/',include("users.urls",namespace="users")),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}, name="login"),
	url(r'^logout/$', 'users.views.log_out', name="logout"),
	# url(r"^contacto/","contactos.views.contacto",name="contacto"),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
