from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from media_objects.models import Image,Document
from levantamiento.models import Levantamiento


class InlineImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ("img",)

class InlineDocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ("doc",)

ImageFormSet = generic_inlineformset_factory(Image,form=InlineImageForm,extra=1,can_delete=False)
DocumentFormSet = generic_inlineformset_factory(Document,form=InlineDocumentForm,extra=1,can_delete=False)