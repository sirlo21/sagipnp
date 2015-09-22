# -*- coding: utf-8 -*-
from django import forms
from metrados.models import *

class FichaTecnicaForm(forms.ModelForm):
	class Meta:
		model = FichaTecnica
		fields = "__all__"
		widgets = {"nombre": forms.TextInput(attrs={"class": "form-control"}),
			"metrado1": forms.Select(attrs={"class": "form-control"}),
			"metrado2": forms.Select(attrs={"class": "form-control"}),
			"metrado3": forms.Select(attrs={"class": "form-control"}),
			"metrado4": forms.Select(attrs={"class": "form-control"}),
			"numero": forms.NumberInput(attrs={"class": "form-control"}),
			"largo": forms.NumberInput(attrs={"class": "form-control"}),
			"ancho": forms.NumberInput(attrs={"class": "form-control"}),
			"alto": forms.NumberInput(attrs={"class": "form-control"}),
			"parcial": forms.NumberInput(attrs={"class": "form-control"}),
			"unidad": forms.NumberInput(attrs={"class": "form-control"}),
			"punitario": forms.NumberInput(attrs={"class": "form-control"})
		}
