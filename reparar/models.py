# -*- coding: utf-8 -*-
from django.db import models
from levantamiento.models import Levantamiento

class TipoDeTecho(models.Model):
	tipo = models.CharField(max_length=250)

	def __unicode__(self):
		return self.tipo

class EstadoDeEjecucion(models.Model):
	estado = models.CharField(max_length=250)

	def __unicode__(self):
		return self.estado

class TipoDeReparacion(models.Model):
	reparacion = models.CharField(max_length=900)

	def __unicode__(self):
		return self.reparacion

class TReparacion(TipoDeReparacion):
	pass

class ISReparacion(TipoDeReparacion):
	pass

class IEReparacion(TipoDeReparacion):
	pass

class MPReparacion(TipoDeReparacion):
	pass

class VEReparacion(TipoDeReparacion):
	pass

class Techo(models.Model):
	techo_descripcion = models.TextField()
	techo_numero_unidad_medida = models.PositiveIntegerField(max_length=20,default=0)
	techo_dimensiones	= models.CharField(max_length=150)
	techo_precio_unitario = models.PositiveIntegerField(default=0)
	techo_precio_total_referencial = models.PositiveIntegerField(default=0)
	techo_tiempo_ejecucion = models.PositiveIntegerField()
	techo_img = models.ImageField(upload_to="images/")
	techo_doc	= models.FileField(upload_to="docs/")
	techo_observaciones = models.TextField(blank=True,null=True)
	techo_estado_ejecucion = models.ForeignKey(EstadoDeEjecucion)
	techo_vigente = models.BooleanField(default=True)
	techo_form = models.ForeignKey(Levantamiento,related_name='techos')
	techo_tipo = models.ForeignKey(TipoDeTecho)
	techo_tipo_reparacion = models.ForeignKey(TReparacion)
	techo_pub_data = models.DateTimeField(auto_now=True)

class InstalacionSanitaria(models.Model):
	inst_sant_descripcion = models.TextField()
	inst_sant_numero_unidad_medida = models.PositiveIntegerField(max_length=20,default=0)
	inst_sant_dimensiones	= models.CharField(max_length=150)
	inst_sant_precio_unitario = models.PositiveIntegerField(default=0)
	inst_sant_precio_total_referencial = models.PositiveIntegerField(default=0)
	inst_sant_tiempo_ejecucion = models.PositiveIntegerField()
	inst_sant_img = models.ImageField(upload_to="images/")
	inst_sant_doc	= models.FileField(upload_to="docs/")
	inst_sant_observaciones = models.TextField(blank=True,null=True)
	inst_sant_estado_ejecucion = models.ForeignKey(EstadoDeEjecucion)
	inst_sant_vigente = models.BooleanField(default=True)
	inst_sant_form = models.ForeignKey(Levantamiento,related_name='instalaciones_sanitarias')
	inst_sant_tipo_reparacion = models.ForeignKey(ISReparacion)
	inst_sant_pub_data = models.DateTimeField(auto_now=True)

class InstalacionElectrica(models.Model):
	inst_elect_descripcion = models.TextField()
	inst_elect_numero_unidad_medida = models.PositiveIntegerField(max_length=20,default=0)
	inst_elect_dimensiones	= models.CharField(max_length=150)
	inst_elect_precio_unitario = models.PositiveIntegerField(default=0)
	inst_elect_precio_total_referencial = models.PositiveIntegerField(default=0)
	inst_elect_tiempo_ejecucion = models.PositiveIntegerField()
	inst_elect_img = models.ImageField(upload_to="images/")
	inst_elect_doc	= models.FileField(upload_to="docs/")
	inst_elect_observaciones = models.TextField(blank=True,null=True)
	inst_elect_estado_ejecucion = models.ForeignKey(EstadoDeEjecucion)
	inst_elect_vigente = models.BooleanField(default=True)
	inst_elect_form = models.ForeignKey(Levantamiento,related_name='instalaciones_electricas')
	inst_elect_tipo_reparacion = models.ForeignKey(IEReparacion)
	inst_elect_pub_data = models.DateTimeField(auto_now=True)

class MurosParedes(models.Model):
	mp_descripcion = models.TextField()
	mp_numero_unidad_medida = models.PositiveIntegerField(max_length=20,default=0)
	mp_dimensiones	= models.CharField(max_length=150)
	mp_precio_unitario = models.PositiveIntegerField(default=0)
	mp_precio_total_referencial = models.PositiveIntegerField(default=0)
	mp_tiempo_ejecucion = models.PositiveIntegerField()
	mp_img = models.ImageField(upload_to="images/")
	mp_doc	= models.FileField(upload_to="docs/")
	mp_observaciones = models.TextField(blank=True,null=True)
	mp_estado_ejecucion = models.ForeignKey(EstadoDeEjecucion)
	mp_vigente = models.BooleanField(default=True)
	mp_form = models.ForeignKey(Levantamiento,related_name='muros_paredes')
	mp_tipo_reparacion = models.ForeignKey(MPReparacion)
	mp_pub_data = models.DateTimeField(auto_now=True)

class VeredaExterior(models.Model):
	ve_descripcion = models.TextField()
	ve_numero_unidad_medida = models.PositiveIntegerField(max_length=20,default=0)
	ve_dimensiones	= models.CharField(max_length=150)
	ve_precio_unitario = models.PositiveIntegerField(default=0)
	ve_precio_total_referencial = models.PositiveIntegerField(default=0)
	ve_tiempo_ejecucion = models.PositiveIntegerField()
	ve_img = models.ImageField(upload_to="images/")
	ve_doc	= models.FileField(upload_to="docs/")
	ve_observaciones = models.TextField(blank=True,null=True)
	ve_estado_ejecucion = models.ForeignKey(EstadoDeEjecucion)
	ve_vigente = models.BooleanField(default=True)
	ve_form = models.ForeignKey(Levantamiento,related_name='veredas_exteriores')
	ve_tipo_reparacion = models.ForeignKey(VEReparacion)
	ve_pub_data = models.DateTimeField(auto_now=True)
