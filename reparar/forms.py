# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.forms import inlineformset_factory
from reparar.models import *
from levantamiento.models import Levantamiento

WIDGETS = {}

class TechoForm(forms.ModelForm):
	class Meta:
		model = Techo
		exclude = ("techo_vigente","techo_pub_data")
		widgets = {
			"techo_tipo": forms.Select(attrs={"class": "form-control"}),
			"techo_tipo_reparacion": forms.Select(attrs={"class": "form-control"}),
			"techo_descripcion": forms.Textarea(attrs={"class": "form-control","placeholder": u"Descripción"}),
			"techo_numero_unidad_medida": forms.NumberInput(attrs={"class": "form-control","placeholder": "Unidad de medida"}),
			"techo_dimensiones": forms.TextInput(attrs={"class": "form-control","placeholder": "Centro Dimensiones"}),
			"techo_precio_unitario": forms.NumberInput(attrs={"class": "form-control","placeholder": "Precio unitario"}),
			"techo_precio_total_referencial": forms.TextInput(attrs={"class": "form-control","value": 0,"readonly": ""}),
			"techo_tiempo_ejecucion": forms.NumberInput(attrs={"class": "form-control","placeholder": "Tiempo de ejecucion"}),
			"techo_observaciones": forms.Textarea(attrs={"class": "form-control","placeholder": "Observaciones"}),
			"techo_estado_ejecucion": forms.Select(attrs={"class": "form-control"}),
		}
		js = ("js/reparar.js")

class InstalacionSanitariaForm(forms.ModelForm):
	class Meta:
		model = InstalacionSanitaria
		exclude = ("inst_sant_vigente","inst_sant_pub_data")
		widgets = {
			"inst_sant_tipo_reparacion": forms.Select(attrs={"class": "form-control"}),
			"inst_sant_descripcion": forms.Textarea(attrs={"class": "form-control","placeholder": u"Descripción"}),
			"inst_sant_numero_unidad_medida": forms.NumberInput(attrs={"class": "form-control","placeholder": "Unidad de medida"}),
			"inst_sant_dimensiones": forms.TextInput(attrs={"class": "form-control","placeholder": "Centro Dimensiones"}),
			"inst_sant_precio_unitario": forms.NumberInput(attrs={"class": "form-control","placeholder": "Precio unitario"}),
			"inst_sant_precio_total_referencial": forms.TextInput(attrs={"class": "form-control","value": 0,"readonly": ""}),
			"inst_sant_tiempo_ejecucion": forms.NumberInput(attrs={"class": "form-control","placeholder": "Tiempo de ejecucion"}),
			"inst_sant_observaciones": forms.Textarea(attrs={"class": "form-control","placeholder": "Observaciones"}),
			"inst_sant_estado_ejecucion": forms.Select(attrs={"class": "form-control"}),
		}
		js = ("js/reparar.js")

class InstalacionElectricaForm(forms.ModelForm):
	class Meta:
		model = InstalacionElectrica
		exclude = ("inst_elect_vigente","inst_elect_pub_data")
		widgets = {
			"inst_elect_tipo_reparacion": forms.Select(attrs={"class": "form-control"}),
			"inst_elect_descripcion": forms.Textarea(attrs={"class": "form-control","placeholder": u"Descripción"}),
			"inst_elect_numero_unidad_medida": forms.NumberInput(attrs={"class": "form-control","placeholder": "Unidad de medida"}),
			"inst_elect_dimensiones": forms.TextInput(attrs={"class": "form-control","placeholder": "Centro Dimensiones"}),
			"inst_elect_precio_unitario": forms.NumberInput(attrs={"class": "form-control","placeholder": "Precio unitario"}),
			"inst_elect_precio_total_referencial": forms.TextInput(attrs={"class": "form-control","value": 0,"readonly": ""}),
			"inst_elect_tiempo_ejecucion": forms.NumberInput(attrs={"class": "form-control","placeholder": "Tiempo de ejecucion"}),
			"inst_elect_observaciones": forms.Textarea(attrs={"class": "form-control","placeholder": "Observaciones"}),
			"inst_elect_estado_ejecucion": forms.Select(attrs={"class": "form-control"}),
		}
		js = ("js/reparar.js")

class MurosParedesForm(forms.ModelForm):
	class Meta:
		model = MurosParedes
		exclude = ("mp_vigente","mp_pub_data")
		widgets = {
			"mp_tipo_reparacion": forms.Select(attrs={"class": "form-control"}),
			"mp_descripcion": forms.Textarea(attrs={"class": "form-control","placeholder": u"Descripción"}),
			"mp_numero_unidad_medida": forms.NumberInput(attrs={"class": "form-control","placeholder": "Unidad de medida"}),
			"mp_dimensiones": forms.TextInput(attrs={"class": "form-control","placeholder": "Centro Dimensiones"}),
			"mp_precio_unitario": forms.NumberInput(attrs={"class": "form-control","placeholder": "Precio unitario"}),
			"mp_precio_total_referencial": forms.TextInput(attrs={"class": "form-control","value": 0,"readonly": ""}),
			"mp_tiempo_ejecucion": forms.NumberInput(attrs={"class": "form-control","placeholder": "Tiempo de ejecucion"}),
			"mp_observaciones": forms.Textarea(attrs={"class": "form-control","placeholder": "Observaciones"}),
			"mp_estado_ejecucion": forms.Select(attrs={"class": "form-control"}),
		}
		js = ("js/reparar.js")

TechoFormSet = inlineformset_factory(Levantamiento,Techo,form=TechoForm,extra=1,can_delete=False)
InstalacionSanitariaFormSet = inlineformset_factory(Levantamiento,InstalacionSanitaria,form=InstalacionSanitariaForm,extra=1,can_delete=False)
InstalacionElectricaFormSet = inlineformset_factory(Levantamiento,InstalacionElectrica,form=InstalacionElectricaForm,extra=1,can_delete=False)
MurosParedesFormSet = inlineformset_factory(Levantamiento,MurosParedes,form=MurosParedesForm,extra=1,can_delete=False)