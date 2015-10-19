from django.conf.urls import patterns,url
from metrados import views

urlpatterns = patterns('',
	url(r"^ficha-tecnica/(?P<id>\d+)/$",views.ficha_tecnica,name="ficha_tecnica"),
	url(r"^reportes/$",views.reportes,name="reportes"),
	url(r"^reportes/(?P<tipo_instalacion>\w+(_\w+)*)/$",views.reportes_tipo_instalacion,name="reportes_tipo_instalacion"),
	url(r"^reportes/(?P<tipo_instalacion>\w+(_\w+)*)/(?P<nombre_instalacion>\w+(_\w+)*)/$",views.reportes_instalacion,name="reportes_instalacion"),
	url(r"^metrado/json/$",views.json,name="metrado_json"),
)