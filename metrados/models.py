from django.db import models

class Metrado1(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()

class Metrado2(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()
	metrado1_id = models.ForeignKey(Metrado1,related_name='metrado_2')

class Metrado3(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()
	metrado2_id = models.ForeignKey(Metrado2,related_name='metrado_3')

class Metrado4(models.Model):
	codigo = models.CharField(max_length=25)
	descripcion = models.TextField()
	metrado3_id = models.ForeignKey(Metrado3,related_name='metrado_4')
