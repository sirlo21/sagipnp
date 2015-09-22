from django.conf.urls import patterns,url
from metrados import views

urlpatterns = patterns('',
	url(r"^ficha-tecnica/(?P<id>\d+)/$",views.ficha_tecnica,name="ficha_tecnica"),
)