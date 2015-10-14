# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category,Instalacion
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo
from metrados.models import *
from metrados.forms import FichaTecnicaForm,UbigeoForm
from metrados.functions import get_json_metrado
from media_objects.forms import ImageFormSet,DocumentFormSet

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
	context = {"next": request.path,"form": UbigeoForm(),}
	if request.GET.get("ubigeo_0",False) > 0:
		pass
	else:
		context["instalaciones"] = []
		for i in Instalacion.objects.all().order_by("instalacion"):
			name = i.instalacion.replace(" ","-")
			context["instalaciones"].append({"instalacion": i.instalacion,"name": name})

	return render(request,"metrados/reportes.html",context)

def reporte_instalacion(request,tipo_instalacion):
	context = {"next": request.path}
	ti = tipo_instalacion.replace("-"," ")
	fichas_tecnicas = []
	for l in Levantamiento.objects.all():
		instalacion = l.tipo_instalacion
		ficha = {}
		if instalacion.instalacion == ti:
			total_total = 0
			for ft in l.ficha_tecnica.all():
				total = ft.numero * ft.parcial
				precio_total = ft.unidad * ft.punitario
				total_total += total
				ficha.update(instalacion=l.nombre_instalacion,total=total,precio_total=precio_total)
				fichas_tecnicas.append(ficha)
	context["fichas_tecnicas"] = fichas_tecnicas
	return render(request,"metrados/reporte_instalacion.html",context)

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
