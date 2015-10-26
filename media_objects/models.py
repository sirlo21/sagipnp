# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Media(models.Model):
	description = models.CharField("Descripción", max_length=400, blank=True)
	date_registration = models.DateTimeField(auto_now_add=True)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	class Meta:
		abstract = True

class Image(Media):
	img = models.ImageField(upload_to="images/")

class Document(Media):
	doc	= models.FileField(upload_to="docs/")
