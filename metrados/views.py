# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo
from metrados.models import *
from metrados.forms import FichaTecnicaForm,UbigeoForm
from metrados.functions import get_json_metrado

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
		if "valid" in post:
			return JsonResponse({"valid": form.is_valid(),"erros": form.errors})
		else:
			if form.is_valid():
				form.save()
				return JsonResponse({"valid": True,"erros": form.errors})
			return JsonResponse({"valid": False,"erros": form.errors})
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

def reportes(request):
	context = {"form": UbigeoForm(),}
	if request.GET.get("ubigeo_0",False) > 0:
		pass
	else:
		context["ths"] = [u"Tipo de instalacion",
			u"Nombre de la instalacion",
			u"Monto asignado general para reparaciones",
			u"Monto proyectado de levantamientos de información",
			u"Saldo Disponible",
			u"se vizualiza en una Tabla y en un Grafico"
		]
		context["tds"] = []
		monto_general_total = 0
		for l in Levantamiento.objects.all().order_by("nombre_instalacion"):
			monto_general_de_reparaciones = 0
			td = "<td>%s</td>" %l.tipo_instalacion.instalacion
			td += "\n<td>%s</td>" %l.nombre_instalacion
			context["tds"].append(td)

	return render(request,"metrados/reportes.html",context)

def json(request):
	context = {}
	if request.GET.get("metrado1_id",False):
		metrado1_id = request.GET["metrado1_id"]
		m1 = Metrado1.objects.get(id=metrado1_id)
		print get_json_metrado(m1.metrado_2)
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
