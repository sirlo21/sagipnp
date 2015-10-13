from django.conf.urls import patterns,url
from metrados import views

urlpatterns = patterns('',
	url(r"^ficha-tecnica/(?P<id>\d+)/$",views.ficha_tecnica,name="ficha_tecnica"),
	url(r"^reportes/$",views.reportes,name="reportes"),
	url(r"^reportes/(?P<tipo_instalacion>\w+(-\w+)*)/$",views.reporte_instalacion,name="reporte_instalacion"),
	url(r"^metrado/json/$",views.json,name="metrado_json"),
)