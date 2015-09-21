from django.conf.urls import patterns,url
from levantamiento import views

urlpatterns = patterns('',
	url(r"^$",views.index,name="index"),
	url(r"^equipo-de-levantamiento/$",views.equipo_de_levantamiento,name="equipo_de_levantamiento"),
	url(r"^acciones-de-prevencion/(?P<id>\d+)/$",views.acciones_de_prevencion,name="acciones_de_prevencion"),
	url(r"^ficha-tecnica/(?P<id>\d+)/$",views.ficha_tecnica,name="ficha_tecnica"),
	url(r"^json/$",views.json,name="json"),
)