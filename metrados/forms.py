# -*- coding: utf-8 -*-
from django import forms
from metrados.models import *
from django.forms import inlineformset_factory
from levantamiento.models import Levantamiento

class FichaTecnicaForm(forms.ModelForm):
	class Meta:
		model = FichaTecnica
		fields = "__all__"
		widgets = {"nombre": forms.TextInput(attrs={"class": "form-control"}),
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