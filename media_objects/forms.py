from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from media_objects.models import Image,Document


class InlineImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = "__all__"

class InlineDocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = "__all__"

ImageFormSet = generic_inlineformset_factory(Image, form=InlineImageForm, extra=1, can_delete=False)
DocumentFormSet = generic_inlineformset_factory(Document, form=InlineDocumentForm, extra=1, can_delete=False)