from django.conf.urls import patterns,url
from levantamiento import views

urlpatterns = patterns('',
	url(r"^$",views.index,name="index"),
	url(r"^equipo-de-levantamiento/$",views.equipo_de_levantamiento,name="equipo_de_levantamiento"),
	url(r"^acciones-de-prevencion/(?P<id>\d+)/$",views.acciones_de_prevencion,name="acciones_de_prevencion"),
	url(r"^equipo-de-levantamiento/json/$",views.json,name="levantamiento_json"),
)