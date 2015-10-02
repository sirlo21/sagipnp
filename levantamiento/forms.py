# -*- coding: utf-8 -*-
import datetime
from django import forms
from ubigeo.fields import UbigeoField
from ubigeo.models import Ubigeo
from levantamiento.models import Levantamiento,RegionPolicial

WIDGETS = {
	"unidad_ejecutora": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"inicio": forms.DateInput(attrs={"class": "form-control"}),
	"termino": forms.DateInput(attrs={"class": "form-control"}),
	"coordinador_equipo": forms.TextInput(attrs={"class": "form-control","placeholder": "Coordinador de equipo","style": "width: 40%;"}),
	"integrante_1": forms.TextInput(attrs={"class": "form-control","placeholder": "Primer integrante","style": "width: 40%;"}),
	"integrante_2": forms.TextInput(attrs={"class": "form-control","placeholder": "Segundo integrante","style": "width: 40%;"}),
	"integrante_3": forms.TextInput(attrs={"class": "form-control","placeholder": "Tercer integrante","style": "width: 40%;"}),
	"centro_poblado": forms.TextInput(attrs={"class": "form-control","placeholder": "Centro poblado","style": "width: 40%;"}),
	"region_policial": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"division": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"tipo_instalacion": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"nombre_instalacion": forms.TextInput(attrs={"class": "form-control","placeholder": "Nombre de la instalacion","style": "width: 40%;"}),
	"direccion_instalacion": forms.TextInput(attrs={"class": "form-control","placeholder": "Direccion de la instalacion","style": "width: 40%;"}),
	"tipo_comisaria": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"clase_comisaria": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"especialidad": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"categoria": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"situacion_del_predio": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"grado": forms.Select(attrs={"class": "form-control","style": "width: 40%;"}),
	"nombre": forms.TextInput(attrs={"class": "form-control","placeholder": "Nombre","style": "width: 40%;"}),
	"apellido": forms.TextInput(attrs={"class": "form-control","placeholder": "Apellido","style": "width: 40%;"}),
	"dni": forms.TextInput(attrs={"class": "form-control","placeholder": "DNI","style": "width: 40%;"}),
	"telefono_fijo_comisaria": forms.TextInput(attrs={"class": "form-control","placeholder": "Telefono fijo de la comisaria","style": "width: 40%;"}),
	"celular_rpc_comisaria": forms.TextInput(attrs={"class": "form-control","placeholder": "Celular RPC de la comisaria","style": "width: 40%;"}),
	"celular_rpm_comisaria": forms.TextInput(attrs={"class": "form-control","placeholder": "Celular RMP de la comisaria","style": "width: 40%;"}),
	"email": forms.EmailInput(attrs={"class": "form-control","placeholder": "Correo electronico","style": "width: 40%;"}),
}

class LevantamientoForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre",required=True,min_length=3,max_length=60,widget=WIDGETS["nombre"])
	apellido = forms.CharField(label="Apellido",required=True,min_length=3,max_length=60,widget=WIDGETS["apellido"])
	dni = forms.CharField(label="DNI",required=True,min_length=8,max_length=8,widget=WIDGETS["dni"])
	telefono_fijo_comisaria = forms.CharField(label="Telefono fijo de la comisaria",required=True,min_length=7,max_length=7,
		widget=WIDGETS["telefono_fijo_comisaria"]
	)
	celular_rpc_comisaria = forms.CharField(label="Celular rpc de la comisaria",required=True,min_length=9,max_length=9,
		widget=WIDGETS["celular_rpc_comisaria"]
	)
	celular_rpm_comisaria = forms.CharField(label="Celular rpm de la comisaria",required=True,min_length=9,max_length=9,
		widget=WIDGETS["celular_rpm_comisaria"]
	)
	email = forms.EmailField(label="Correo electronico",required=True,widget=WIDGETS["email"])
	ubigeo = UbigeoField(
		attrs_1={"required": "", "class": "form-control", "style": "width: 30%; display: inline;"},
		attrs_2={"required": "", "class": "form-control", "style": "width: 35%; display: inline;"},
		attrs_3={"required": "", "class": "form-control", "style": "width: 35%; display: inline;"}
	)

	class Meta:
		model = Levantamiento
		fields = "__all__"
		widgets = WIDGETS

	class Media:
		js = ('js/ubigeo.js','js/select_ubigeo.js')

class ConsultasForm(forms.Form):
	region_policial = forms.ModelChoiceField(
		queryset=RegionPolicial.objects.all(),
		empty_label="Seleccione una región",
		required=False,
		widget=forms.Select(attrs={"class": "form-control"})
	)
