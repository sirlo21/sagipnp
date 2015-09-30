# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo
from metrados.models import *
from metrados.forms import FichaTecnicaForm

@login_required
def ficha_tecnica(request,id):
	levantamiento = Levantamiento.objects.get(id=id)
	distrito = levantamiento.ubigeo
	provincia = Ubigeo.objects.get(id=distrito.parent_id)
	departamento = Ubigeo.objects.get(id=provincia.parent_id)
	context = {"obj": levantamiento,"distrito": distrito,"provincia": provincia,"departamento": departamento}
	if request.method == "POST":
		post = request.POST
		form = FichaTecnicaForm(post)
		if post["valid"] == "true":
			return JsonResponse({"valid": form.is_valid(),"erros": form.errors})
		else:
			if form.is_valid():
				form.save()
				return redirect("/")
			else:
				context["form"] = form
	else:
		context["form"] = FichaTecnicaForm(initial={"form": id})
		context["metrados"] = []
		for metrado2 in Metrado2.objects.all():
			context["metrados"].append({"id": metrado2.id,"codigo": metrado2.codigo,"descripcion": metrado2.descripcion})
		for metrado3 in Metrado3.objects.all():
			context["metrados"].append({"id": metrado3.id,"codigo": metrado3.codigo,"descripcion": metrado3.descripcion})
		for metrado4 in Metrado4.objects.all():
			context["metrados"].append({"id": metrado4.id,"codigo": metrado4.codigo,"descripcion": metrado4.descripcion})
		
	return render(request,"metrados/ficha_tecnica.html",context)

def json(request):
	context = {}
	if request.GET.get("metrado1_id",False):
		metrado1_id = request.GET["metrado1_id"]
		context["metrado2"] = []
		for metrado2 in Metrado1.objects.get(id=metrado1_id).metrado_2.all():
			context["metrado2"].append({"id": metrado2.id,"codigo": metrado2.codigo,"descripcion": metrado2.descripcion})
	elif request.GET.get("metrado2_id",False):
		metrado2_id = request.GET["metrado2_id"]
		context["metrado3"] = []
		for metrado3 in Metrado2.objects.get(id=metrado2_id).metrado_3.all():
			context["metrado3"].append({"id": metrado3.id,"codigo": metrado3.codigo,"descripcion": metrado3.descripcion})
	elif request.GET.get("metrado3_id",False):
		metrado3_id = request.GET["metrado3_id"]
		context["metrado4"] = []
		for metrado4 in Metrado3.objects.get(id=metrado3_id).metrado_4.all():
			context["metrado4"].append({"id": metrado4.id,"codigo": metrado4.codigo,"descripcion": metrado4.descripcion})

	if request.GET.get("metrados",False):
		context["metrado2"] = []
		for metrado2 in Metrado2.objects.all():
			context["metrado2"].append({"id": metrado2.id,"codigo": metrado2.codigo,"descripcion": metrado2.descripcion})
		context["metrado3"] = []
		for metrado3 in Metrado3.objects.all():
			context["metrado3"].append({"id": metrado3.id,"codigo": metrado3.codigo,"descripcion": metrado3.descripcion})
		context["metrado4"] = []
		for metrado4 in Metrado4.objects.all():
			context["metrado4"].append({"id": metrado4.id,"codigo": metrado4.codigo,"descripcion": metrado4.descripcion})

	if request.GET.get("rollback",False):
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
		elif metrado3:
			for m3 in metrado3:
				m2 = m3.metrado2
				m1 = m2.metrado1
				context["rollback"]["metrado1_id"] = m1.id
				context["rollback"]["metrado2_id"] = m2.id
				context["rollback"]["metrado3_id"] = m3.id
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
