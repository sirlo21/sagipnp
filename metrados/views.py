# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category,Instalacion
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo
from metrados.models import *
from metrados.forms import FichaTecnicaForm,SearchForm
from metrados.functions import get_json_metrado
from media_objects.forms import ImageFormSet,DocumentFormSet
from django.core.urlresolvers import reverse

@login_required
def ficha_tecnica(request,id):
	levantamiento = Levantamiento.objects.get(id=id)
	distrito = levantamiento.ubigeo
	provincia = Ubigeo.objects.get(id=distrito.parent_id)
	departamento = Ubigeo.objects.get(id=provincia.parent_id)
	context = {"obj": levantamiento,"distrito": distrito,"provincia": provincia,"departamento": departamento}
	if request.method == "POST":
		post = request.POST
		files = request.FILES
		form = FichaTecnicaForm(post)
		if "valid" in post:
			errors = form.errors
			valid = form.is_valid()
			if form.is_valid():
				errors = []
				obj = form.save(commit=False)
				img_formset = ImageFormSet(post,files,instance=obj,prefix="img_frm")
				if not img_formset.is_valid():
					errors += img_formset.errors
				doc_formset = DocumentFormSet(post,files,instance=obj,prefix="doc_frm")
				if not doc_formset.is_valid():
					errors += doc_formset.errors
				valid = form.is_valid() and img_formset.is_valid() and doc_formset.is_valid()
			return JsonResponse({"valid": valid,"errors": errors})
		else:
			if form.is_valid():
				obj = form.save(commit=False)
				img_formset = ImageFormSet(post,files,instance=obj,prefix="img_frm")
				doc_formset = DocumentFormSet(post,files,instance=obj,prefix="doc_frm")
				if img_formset.is_valid():
					obj.save()
					img_formset.save()
					if doc_formset.is_valid():
						doc_formset.save()
				return JsonResponse({"valid": True,"errors": form.errors})
			return JsonResponse({"valid": False,"errors": form.errors})
	else:
		context["form"] = FichaTecnicaForm(initial={"form": id})
		context["img_formset"] = ImageFormSet(prefix="img_frm")
		context["doc_formset"] = DocumentFormSet(prefix="doc_frm")
		context["metrados"] = []
		for metrado2 in Metrado2.objects.all():
			context["metrados"].append({"id": metrado2.id,"codigo": metrado2.codigo,"descripcion": metrado2.descripcion})
		for metrado3 in Metrado3.objects.all():
			context["metrados"].append({"id": metrado3.id,"codigo": metrado3.codigo,"descripcion": metrado3.descripcion})
		for metrado4 in Metrado4.objects.all():
			context["metrados"].append({"id": metrado4.id,"codigo": metrado4.codigo,"descripcion": metrado4.descripcion})
	context["next"] = request.path
	return render(request,"metrados/ficha_tecnica.html",context)

def reportes(request):
	context = {"next": request.path}
	context["instalaciones"] = []
	for i in Instalacion.objects.all().order_by("instalacion"):
		name = i.instalacion.replace(" ","_")
		context["instalaciones"].append({"instalacion": i.instalacion,"name": name})

	return render(request,"metrados/reportes.html",context)

def reportes_tipo_instalacion(request,tipo_instalacion):
	context = {"next": request.path}
	ti = tipo_instalacion.replace("_"," ")
	fichas_tecnicas = []
	ptotal = 0
	form = SearchForm(request.GET)
	if form.is_valid():
		ubigeo = form.cleaned_data["ubigeo"]
		nombre_instalacion = form.cleaned_data["nombre_instalacion"]
		levantamiento = []
		if ubigeo is not None:
			if nombre_instalacion != "" and not nombre_instalacion.isspace():
				levantamiento = Levantamiento.objects.filter(ubigeo=ubigeo,nombre_instalacion=nombre_instalacion)
			else:
				levantamiento = Levantamiento.objects.filter(ubigeo=ubigeo)
		elif nombre_instalacion != "" and not nombre_instalacion.isspace():
			print form.cleaned_data
			levantamiento = Levantamiento.objects.filter(nombre_instalacion=nombre_instalacion)
		else:
			levantamiento = Levantamiento.objects.all()
		for l in levantamiento:
			instalacion = l.tipo_instalacion
			total = 0
			if instalacion.instalacion == ti and len(l.ficha_tecnica.all()) > 0:
				for ft in l.ficha_tecnica.all():
					total += ft.unidad * ft.punitario
					ptotal += total
				ni = l.nombre_instalacion
				url = request.path+ni.replace(" ","_")
				fichas_tecnicas.append({"instalacion": "<a class='link' href='"+url+"'>"+ni+"</a>",
					"total": total
				})
				context["ptotal"] = ptotal
	context["form"] = SearchForm()
	context["fichas_tecnicas"] = fichas_tecnicas
	return render(request,"metrados/reportes_tipo_instalacion.html",context)

def reportes_instalacion(request,tipo_instalacion,nombre_instalacion):
	context = {"next": request.path}
	ti = tipo_instalacion.replace("_"," ")
	ni = nombre_instalacion.replace("_"," ")
	fichas_tecnicas = []
	ptotal = 0
	for l in Levantamiento.objects.filter(nombre_instalacion=ni):
		total = 0
		if l.tipo_instalacion.instalacion == ti and len(l.ficha_tecnica.all()) > 0:
			for ft in l.ficha_tecnica.all():
				total = ft.numero * ft.parcial
				pt = ft.unidad * ft.punitario
				ptotal += pt
				if ft.metrado4.descripcion == "N/A":
					if ft.metrado3.descripcion == "N/A":
						partida = ft.metrado2
					else:
						partida = ft.metrado3
				else:
					partida = ft.metrado4
			ni = l.nombre_instalacion
			dic = {"partida": partida,"nv": ft.numero,"dl": ft.largo,"da": ft.ancho,"dh": ft.alto,
				"parcial": ft.parcial,"total": total,"unidad": ft.unidad,"pu": ft.punitario,"pt": pt
			}
			fichas_tecnicas.append(dic)
			context["ptotal"] = ptotal
			break
	context["form"] = SearchForm()
	context["fichas_tecnicas"] = fichas_tecnicas
	context["tipo_instalacion"] = tipo_instalacion
	context["range"] = range(0,len(fichas_tecnicas[0])-2)
	return render(request,"metrados/reportes_instalacion.html",context)

def json(request):
	context = {}
	if request.GET.get("metrado1_id",False):
		metrado1_id = request.GET["metrado1_id"]
		m1 = Metrado1.objects.get(id=metrado1_id)
		context["metrado2"] = get_json_metrado(m1.metrado_2)
	elif request.GET.get("metrado2_id",False):
		metrado2_id = request.GET["metrado2_id"]
		m2 = Metrado2.objects.get(id=metrado2_id)
		context["metrado3"] = get_json_metrado(m2.metrado_3)
	elif request.GET.get("metrado3_id",False):
		metrado3_id = request.GET["metrado3_id"]
		m3 = Metrado3.objects.get(id=metrado3_id)
		context["metrado4"] = get_json_metrado(m3.metrado_4)
	elif request.GET.get("metrados",False):
		context["metrado2"] = []
		for metrado2 in Metrado2.objects.all():
			context["metrado2"].append({"id": metrado2.id,"codigo": metrado2.codigo,"descripcion": metrado2.descripcion})
		context["metrado3"] = []
		for metrado3 in Metrado3.objects.all():
			context["metrado3"].append({"id": metrado3.id,"codigo": metrado3.codigo,"descripcion": metrado3.descripcion})
		context["metrado4"] = []
		for metrado4 in Metrado4.objects.all():
			context["metrado4"].append({"id": metrado4.id,"codigo": metrado4.codigo,"descripcion": metrado4.descripcion})
	elif request.GET.get("rollback",False):
		rollback = request.GET["rollback"].upper()
		metrado2 = Metrado2.objects.filter(descripcion=rollback)
		metrado3 = Metrado3.objects.filter(descripcion=rollback)
		metrado4 = Metrado4.objects.filter(descripcion=rollback)
		context["rollback"] = {}
		if metrado2:
			for m2 in metrado2:
				m1 = m2.metrado1
				context["rollback"]["metrado1_id"] = m1.id
				context["rollback"]["metrado2_id"] = m2.id
				if len(m2.metrado_3.all()) == 1:
					m3 = m2.metrado_3.all()[0]
					m4 = m3.metrado_4.all()[0]
					context["rollback"]["metrado3_id"] = m3.id
					context["rollback"]["metrado4_id"] = m4.id
		elif metrado3:
			for m3 in metrado3:
				m2 = m3.metrado2
				m1 = m2.metrado1
				context["rollback"]["metrado1_id"] = m1.id
				context["rollback"]["metrado2_id"] = m2.id
				context["rollback"]["metrado3_id"] = m3.id
				if len(m3.metrado_4.all()) == 1:
					m4 = m3.metrado_4.all()[0]
					context["rollback"]["metrado4_id"] = m4.id
		elif metrado4:
			for m4 in metrado4:
				m3 = m4.metrado3
				m2 = m3.metrado2
				m1 = m2.metrado1

				context["rollback"]["metrado1_id"] = m1.id
				context["rollback"]["metrado2_id"] = m2.id
				context["rollback"]["metrado3_id"] = m3.id
				context["rollback"]["metrado4_id"] = m4.id
	return JsonResponse(context)
