from django.db import models

class Image(models.Model):
	img = models.ImageField(upload_to="images/")

class Document(models.Model):
	doc	= models.FileField(upload_to="docs/")
