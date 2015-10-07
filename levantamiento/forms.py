# -*- coding: utf-8 -*-
import datetime
from django import forms
from ubigeo.fields import UbigeoField
from ubigeo.models import Ubigeo
from levantamiento.models import Levantamiento,RegionPolicial

WIDGETS = {
	"unidad_ejecutora": forms.Select(attrs={"class": "form-control"}),
	"inicio": forms.DateInput(attrs={"class": "form-control"}),
	"termino": forms.DateInput(attrs={"class": "form-control"}),
	"coordinador_equipo": forms.TextInput(attrs={"class": "form-control","placeholder": "Coordinador de equipo"}),
	"integrante_1": forms.TextInput(attrs={"class": "form-control","placeholder": "Primer integrante"}),
	"integrante_2": forms.TextInput(attrs={"class": "form-control","placeholder": "Segundo integrante"}),
	"integrante_3": forms.TextInput(attrs={"class": "form-control","placeholder": "Tercer integrante"}),
	"centro_poblado": forms.TextInput(attrs={"class": "form-control","placeholder": "Centro poblado"}),
	"region_policial": forms.Select(attrs={"class": "form-control"}),
	"division": forms.Select(attrs={"class": "form-control"}),
	"tipo_instalacion": forms.Select(attrs={"class": "form-control"}),
	"nombre_instalacion": forms.TextInput(attrs={"class": "form-control","placeholder": "Nombre de la instalacion"}),
	"direccion_instalacion": forms.TextInput(attrs={"class": "form-control","placeholder": "Direccion de la instalacion"}),
	"monto": forms.NumberInput(attrs={"class": "form-control","placeholder": "Direccion de la instalacion"}),
	"tipo_comisaria": forms.Select(attrs={"class": "form-control"}),
	"clase_comisaria": forms.Select(attrs={"class": "form-control"}),
	"especialidad": forms.Select(attrs={"class": "form-control"}),
	"categoria": forms.Select(attrs={"class": "form-control"}),
	"situacion_del_predio": forms.Select(attrs={"class": "form-control"}),
	"grado": forms.Select(attrs={"class": "form-control"}),
	"nombre": forms.TextInput(attrs={"class": "form-control","placeholder": "Nombre"}),
	"apellido": forms.TextInput(attrs={"class": "form-control","placeholder": "Apellido"}),
	"dni": forms.TextInput(attrs={"class": "form-control","placeholder": "DNI"}),
	"telefono_fijo_comisaria": forms.TextInput(attrs={"class": "form-control","placeholder": "Telefono fijo de la comisaria"}),
	"celular_rpc_comisaria": forms.TextInput(attrs={"class": "form-control","placeholder": "Celular RPC de la comisaria"}),
	"celular_rpm_comisaria": forms.TextInput(attrs={"class": "form-control","placeholder": "Celular RMP de la comisaria"}),
	"email": forms.EmailInput(attrs={"class": "form-control","placeholder": "Correo electronico"}),
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
