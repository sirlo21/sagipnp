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
		form = FichaTecnicaFormSet(post,instance=levantamiento)
		if form.is_valid():
			form.save()
			return redirect("/")
		else:
			context["fiche_tecnica_form"] = form
	else:
		context["fiche_tecnica_form"] = FichaTecnicaFormSet()
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

	if request.GET.get("metrado",False):
		metrado = request.GET["metrado"].upper()
		metrado2 = Metrado2.objects.filter
		if metrado2(descripcion=metrado):
			metrado2 = metrado2(descripcion=metrado)
		else:
			metrado2 = metrado2(descripcion=metrado+" ")
		metrado3 = Metrado3.objects.filter
		if metrado3(descripcion=metrado):
			metrado3 = metrado3(descripcion=metrado)
		else:
			metrado3 = metrado3(descripcion=metrado+" ")
		metrado4 = Metrado4.objects.filter
		if metrado4(descripcion=metrado):
			print metrado4
			print 1
			metrado4 = metrado4(descripcion=metrado)
		else:
			metrado4 = metrado4(descripcion=metrado+" ")
			print metrado
			print metrado4(descripcion=metrado+" ")
			print 2	
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
