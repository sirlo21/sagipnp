from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Media(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

class Image(Media):
	img = models.ImageField(upload_to="images/")

class Document(Media):
	doc	= models.FileField(upload_to="docs/")
