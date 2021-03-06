from django.conf.urls import patterns,url
from ayudas import views

urlpatterns = patterns('',
	url(r"^$",views.index,name="ayuda_index"),
	url(r"^edit/(?P<form>\w+(.\w)*)$",views.edit,name="ayuda_edit"),
	url(r"^show/(?P<form>\w+(.\w)*)/(?P<posicion>\d+)/$",views.show,name="show_ayuda"),
)