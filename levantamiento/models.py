# -*- coding: utf-8 -*-
from django.db import models
from ubigeo.models import Ubigeo

class TComisaria(models.Model):
	tipo = models.CharField(max_length=250)

	def __unicode__(self):
		return self.tipo

class CComisaria(models.Model):
	clase = models.CharField(max_length=250)

	def __unicode__(self):
		return self.clase

class Especialidad(models.Model):
	especialidad = models.CharField(max_length=250)

	def __unicode__(self):
		return self.especialidad

class Category(models.Model):
	category = models.CharField(max_length=250)

	def __unicode__(self):
		return self.category

class SituacionLegal(models.Model):
	situacion = models.CharField(max_length=250)

	def __unicode__(self):
		return self.situacion

class RegionPolicial(models.Model):
	region = models.CharField(max_length=250)

	def __unicode__(self):
		return self.region

class DivisionPolicial(models.Model):
	division = models.CharField(max_length=250)

	def __unicode__(self):
		return self.division

class Grado(models.Model):
	grado = models.CharField(max_length=150)

	def __unicode__(self):
		return self.grado

class UnidadEjecutora(models.Model):
	unidad = models.CharField(max_length=150)

	def __unicode__(self):
		return self.unidad

class Instalacion(models.Model):
	instalacion = models.CharField(max_length=500)

	def __unicode__(self):
		return self.instalacion

class Levantamiento(models.Model):
	unidad_ejecutora = models.ForeignKey(UnidadEjecutora,related_name='formularios')
	inicio = models.DateField()
	termino = models.DateField()
	coordinador_equipo = models.CharField(max_length=300)
	integrante_1 = models.CharField(max_length=300)
	integrante_2 = models.CharField(max_length=300)
	integrante_3 = models.CharField(max_length=300)
	ubigeo = models.ForeignKey(Ubigeo,related_name='formularios')
	centro_poblado = models.CharField(max_length=1000)
	region_policial = models.ForeignKey(RegionPolicial,related_name='formularios',blank=True,null=True)
	division = models.ForeignKey(DivisionPolicial,related_name='formularios',blank=True,null=True)
	tipo_instalacion = models.ForeignKey(Instalacion,related_name='formulario')
	nombre_instalacion = models.CharField(max_length=300)
	direccion_instalacion = models.CharField(max_length=500)
	ejecutando_mejoras_mantenimiento = models.NullBooleanField(null=True)
	monto = models.IntegerField(default=0,blank=True,null=True)
	tipo_comisaria = models.ForeignKey(TComisaria,related_name='formularios',blank=True,null=True)
	clase_comisaria = models.ForeignKey(CComisaria,related_name='formularios',blank=True,null=True)
	especialidad = models.ForeignKey(Especialidad,related_name='formularios',blank=True,null=True)
	categoria = models.ForeignKey(Category,related_name='formularios',blank=True,null=True)
	situacion_del_predio = models.ForeignKey(SituacionLegal,related_name='formularios',blank=True,null=True)
	grado = models.ForeignKey(Grado,related_name='formularios',blank=True,null=True)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	dni = models.CharField(max_length=8)
	telefono_fijo_comisaria = models.CharField(max_length=10)
	celular_rpc_comisaria = models.CharField(max_length=9)
	celular_rpm_comisaria = models.CharField(max_length=9)
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombre
