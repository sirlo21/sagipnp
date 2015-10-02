# -*- coding: utf-8 -*-
from django import forms
from metrados.models import *
from django.forms import inlineformset_factory
from levantamiento.models import Levantamiento,Instalacion
from ubigeo.fields import UbigeoField
from ubigeo.models import Ubigeo

class FichaTecnicaForm(forms.ModelForm):
	class Meta:
		model = FichaTecnica
		fields = "__all__"
		widgets = {
			"form": forms.HiddenInput(),
			"nombre": forms.TextInput(attrs={"class": "form-control"}),
			"metrado1": forms.Select(attrs={"class": "form-control"}),
			"metrado2": forms.Select(attrs={"class": "form-control"}),
			"metrado3": forms.Select(attrs={"class": "form-control"}),
			"metrado4": forms.Select(attrs={"class": "form-control"}),
			"numero": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0}),
			"largo": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0}),
			"ancho": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0}),
			"alto": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0}),
			"parcial": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0}),
			"unidad": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0}),
			"punitario": forms.NumberInput(attrs={"class": "form-control","min": 0,"value": 0})
		}

class UbigeoForm(forms.Form):
	CONSULTA_CHOICES = ((1,u"Consulta financiera de las reparaciones"),
		(2,u"Consulta de Numero y relación de Instalaciones intervenidas"),
		(3,u"Estado de las acciones de prevención")
	)
	TIPO_INSTALACION_CHOICES = []
	for instalacion in Instalacion.objects.all():
		TIPO_INSTALACION_CHOICES.append((instalacion.id,instalacion.instalacion))
	ubigeo = UbigeoField(
		attrs_1={"class": "form-control", "style": "width: 30%; display: inline;"},
		attrs_2={"class": "form-control", "style": "width: 35%; display: inline;"},
		attrs_3={"class": "form-control", "style": "width: 35%; display: inline;"}
	)
	tipo_instalacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),choices=TIPO_INSTALACION_CHOICES)
	consulta = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),choices=CONSULTA_CHOICES)

	class Media:
		js = ('js/ubigeo.js','js/select_ubigeo.js')
