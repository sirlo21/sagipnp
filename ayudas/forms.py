from django import forms
from django.forms import modelformset_factory
from ayudas.models import Ayuda

class AyudaForm(forms.ModelForm):
	class Meta:
		model = Ayuda
		exclude = ("form",)
		widgets = {"posicion": forms.NumberInput(attrs={"class": "form-control","placeholder": "Posicion","min": 0,"value": 0}),
			"title": forms.TextInput(attrs={"class": "form-control","placeholder": "Titulo"}),
			"text": forms.Textarea(attrs={"class": "form-control","placeholder":"Texto de ayuda"})
		}

AyudaFormSet = modelformset_factory(Ayuda,form=AyudaForm,extra=1,can_delete=True)