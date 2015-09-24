# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo
from metrados.models import *
from metrados.forms import FichaTecnicaFormSet

@login_required
def ficha_tecnica(request,id):
	levantamiento = Levantamiento.objects.get(id=id)
	distrito = levantamiento.ubigeo
	provincia = Ubigeo.objects.get(id=distrito.parent_id)
	departamento = Ubigeo.objects.get(id=provincia.parent_id)
	context = {"obj": levantamiento,"distrito": distrito,"provincia": provincia,"departamento": departamento}
	if request.method == "POST":
		post = request.POST
		form = FichaTecnicaFormSet(request.POST,instance=levantamiento)
		if form.is_valid():
			form.save()
			return redirect("/")
		else:
			context["fiche_tecnica_form"] = form
	else:
		context["fiche_tecnica_form"] = FichaTecnicaFormSet()
		
	return render(request,"metrados/ficha_tecnica.html",context)

def json(request):
	context = {}
	if request.GET.get("metrado1_id",False):
		metrado1_id = request.GET["metrado1_id"]
		context["metrado2"] = []
		for metrado2 in Metrado2.objects.filter(metrado1_id=metrado1_id):
			context["metrado2"].append({"id": metrado2.id,"codigo": metrado2.codigo,"descripcion": metrado2.descripcion})
	elif request.GET.get("metrado2_id",False):
		metrado2_id = request.GET["metrado2_id"]
		context["metrado3"] = []
		for metrado3 in Metrado3.objects.filter(metrado2_id=metrado2_id):
			context["metrado3"].append({"id": metrado3.id,"codigo": metrado3.codigo,"descripcion": metrado3.descripcion})
	elif request.GET.get("metrado3_id",False):
		metrado3_id = request.GET["metrado3_id"]
		context["metrado4"] = []
		for metrado4 in Metrado4.objects.filter(metrado3_id=metrado3_id):
			context["metrado4"].append({"id": metrado4.id,"codigo": metrado4.codigo,"descripcion": metrado4.descripcion})
	return JsonResponse(context)
