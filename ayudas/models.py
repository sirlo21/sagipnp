from django.db import models

class Ayuda(models.Model):
	form = models.CharField(max_length=300)
	posicion = models.IntegerField(blank=True,null=True)
	title = models.CharField(max_length=40,blank=True)
	text = models.TextField(blank=True)
	pub_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title
