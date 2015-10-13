from django.db import models
from levantamiento.models import Levantamiento
from media_objects.models import Image,Document
from django.contrib.contenttypes.fields import GenericRelation

class Metrado1(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.descripcion

class Metrado2(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()
	metrado1 = models.ForeignKey(Metrado1,related_name='metrado_2')

	def __unicode__(self):
		return self.descripcion

class Metrado3(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()
	metrado2 = models.ForeignKey(Metrado2,related_name='metrado_3')

	def __unicode__(self):
		return self.descripcion

class Metrado4(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()
	metrado3 = models.ForeignKey(Metrado3,related_name='metrado_4')

	def __unicode__(self):
		return self.descripcion

class FichaTecnica(models.Model):
	form  = models.ForeignKey(Levantamiento,related_name='ficha_tecnica')
	metrado1 = models.ForeignKey(Metrado1,related_name='ficha_tecnica')
	metrado2 = models.ForeignKey(Metrado2,related_name='ficha_tecnica')
	metrado3 = models.ForeignKey(Metrado3,related_name='ficha_tecnica')
	metrado4 = models.ForeignKey(Metrado4,related_name='ficha_tecnica')
	images = GenericRelation(Image,null=False,blank=False)
	docs = GenericRelation(Document,null=True,blank=True)
	numero = models.IntegerField(default=0)
	largo = models.FloatField(default=0)
	ancho = models.FloatField(default=0)
	alto = models.FloatField(default=0)
	parcial = models.IntegerField(default=0)
	unidad = models.IntegerField(default=0)
	punitario = models.IntegerField(default=0)

	def __unicode__(self):
		return self.form.nombre
