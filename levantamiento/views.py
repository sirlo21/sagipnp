from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category
from reparar.models import Techo,InstalacionSanitaria,InstalacionElectrica,MurosParedes
from levantamiento.forms import LevantamientoForm,ConsultasForm
from reparar.forms import (TechoFormSet,InstalacionSanitariaFormSet,InstalacionElectricaFormSet,MurosParedesFormSet,
	VeredaExteriorFormSet)
from ayudas.models import Ayuda
from datetime import datetime
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo

@login_required
def index(request):
	ayudas = Ayuda.objects.filter(form="portada")
	context = {"next": request.path,"ayudas": ayudas}
	return render(request,"levantamiento/index.html",context)

@login_required
def equipo_de_levantamiento(request):
	context = {"next": request.path}
	if request.method == "POST":
		form = LevantamientoForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			techos = request.POST["techos"]
			if techos == "on":
				context["techos"] = techos
			inst_sant = request.POST["inst_sant"]
			if inst_sant == "on":
				context["inst_sant"] = inst_sant
			inst_elect = request.POST["inst_elect"]
			if inst_elect == "on":
				context["inst_elect"] = inst_elect
			muros_paredes = request.POST["muros_paredes"]
			if muros_paredes == "on":
				context["muros_paredes"] = muros_paredes
			if techos == "on" or inst_sant == "on" or inst_elect == "on" or muros_paredes == "on":
				techo_form_ayuda = "techos"
				inst_sant_form_ayuda = "instalaciones_sanitarias"
				inst_elect_form_ayuda = "instalaciones_electricas"
				muros_paredes_form_ayuda = "muros_y_paredes"
				veredas_exteriores_form_ayuda = "veredas_exteriores"
				
				context["techo_form"] = TechoFormSet()
				context["inst_sant_form"] = InstalacionSanitariaFormSet()
				context["inst_elect_form"] = InstalacionElectricaFormSet()
				context["muros_paredes_form"] = MurosParedesFormSet()
				context["veredas_exteriores_form"] = VeredaExteriorFormSet()
				context["form_id"] = obj.id
				context["techo_form_ayuda"] = techo_form_ayuda
				context["inst_sant_form_ayuda"] = inst_sant_form_ayuda
				context["inst_elect_form_ayuda"] = inst_elect_form_ayuda
				context["muros_paredes_form_ayuda"] = muros_paredes_form_ayuda
				context["veredas_exteriores_form_ayuda"] = veredas_exteriores_form_ayuda
				context["techos_posicion_ayuda"] = posiciones_de_ayuda(techo_form_ayuda)
				context["inst_sant_posicion_ayuda"] = posiciones_de_ayuda(inst_sant_form_ayuda)
				context["inst_elect_posicion_ayuda"] = posiciones_de_ayuda(inst_elect_form_ayuda)
				context["mp_posicion_ayuda"] = posiciones_de_ayuda(muros_paredes_form_ayuda)
				context["ve_posicion_ayuda"] = posiciones_de_ayuda(veredas_exteriores_form_ayuda)
				return render(request,"levantamiento/acciones_de_prevencion.html",context)
			return redirect("/")
		context["form"] = form
	else:
		context["form"] = LevantamientoForm(initial={"inicio": datetime.today(),"termino": datetime.today()})
	form_ayuda = "levantamiento_de_informacion"
	context["form_ayuda"] = form_ayuda
	context["posicion_ayuda"] = posiciones_de_ayuda(form_ayuda)
	return render(request,"levantamiento/equipo_de_levantamiento.html",context)

@login_required
def acciones_de_prevencion(request,id):
	if request.method == "POST" or request.method == "GET":
		post = request.POST
		context = {"next": request.path}
		obj = Levantamiento.objects.get(id=id)
		techos = post.get("techos",False)
		if techos:
			context["techos"] = techos
			tch = TechoFormSet(post,request.FILES,instance=obj)
			if tch.is_valid():
				tch.save()
				tch_save = True
			else:
				tch_save = False
				context["techo_form"] = tch
		else:
			tch_save = True

		inst_sant = post.get("inst_sant",False)
		if inst_sant:
			context["inst_sant"] = inst_sant
			inst = InstalacionSanitariaFormSet(post,request.FILES,instance=obj)
			if inst.is_valid():
				inst.save()
				inst_save = True
			else:
				inst_save = False
				context["inst_sant_form"] = inst
		else:
			inst_save = True
	
		inst_elect = post.get("inst_elect",False)
		if inst_elect:
			context["inst_elect"] = inst_elect
			inel = InstalacionElectricaFormSet(post,request.FILES,instance=obj)
			if inel.is_valid():
				inel.save()
				inel_save = True
			else:
				inel_save = False
				context["inst_elect_form"] = inel
		else:
			inel_save = True

		muros_paredes = post.get("muros_paredes",False)
		if muros_paredes:
			context["muros_paredes"] = muros_paredes
			mp = MurosParedesFormSet(post,request.FILES,instance=obj)
			if mp.is_valid():
				mp.save()
				mp_save = True
			else:
				mp_save = False
				context["muros_paredes_form"] = mp
		else:
			mp_save = True

		veredas_exteriores = post.get("veredas_exteriores",False)
		if veredas_exteriores:
			context["veredas_exteriores"] = veredas_exteriores
			ve = VeredaExteriorFormSet(post,request.FILES,instance=obj)
			if ve.is_valid():
				ve.save()
				ve_save = True
			else:
				ve_save = False
				context["veredas_exteriores_form"] = ve
		else:
			ve_save = True

		if tch_save and inst_save and inel_save and mp_save and ve_save:
			return render(request,"reparar/ficha_tecnica.html",context)
		context["form_id"] = id
		return render(request,"levantamiento/acciones_de_prevencion.html",context)
	return redirect("/")

def json(request):
	context = {}
	if request.GET.get("tipo_instalacion",False) == "3":
		context["tipo_comisaria"] = []
		context["clase_comisaria"] = []
		context["especialidad"] = []
		context["categoria"] = []
		for tipo in TComisaria.objects.all():
			context["tipo_comisaria"].append({"id": tipo.id,"name": tipo.tipo})
		for clase in CComisaria.objects.all():
			context["clase_comisaria"].append({"id": clase.id,"name": clase.clase})
		for especialidad in Especialidad.objects.all():
			context["especialidad"].append({"id": especialidad.id,"name": especialidad.especialidad})
		for categoria in Category.objects.all():
			context["categoria"].append({"id": categoria.id,"name": categoria.category})
	return JsonResponse(context)

# @login_required
def ficha_tecnica(request,id):
	levantamiento = Levantamiento.objects.get(id=id)
	distrito = levantamiento.ubigeo
	provincia = Ubigeo.objects.get(id=distrito.parent_id)
	departamento = Ubigeo.objects.get(id=provincia.parent_id)
	context = {"obj": levantamiento,"departamento": departamento,"provincia": provincia,"distrito": distrito}
	return render(request,"reparar/ficha_tecnica.html",context)
