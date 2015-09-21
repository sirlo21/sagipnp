from django.shortcuts import render,redirect
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category
from reparar.models import Techo,InstalacionSanitaria,InstalacionElectrica,MurosParedes
from levantamiento.forms import LevantamientoForm,ConsultasForm
from reparar.forms import TechoFormSet,InstalacionSanitariaFormSet,InstalacionElectricaFormSet,MurosParedesFormSet
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
				
				context["techo_form"] = TechoFormSet()
				context["inst_sant_form"] = InstalacionSanitariaFormSet()
				context["inst_elect_form"] = InstalacionElectricaFormSet()
				context["muros_paredes_form"] = MurosParedesFormSet()
				context["form_id"] = obj.id
				context["techo_form_ayuda"] = techo_form_ayuda
				context["inst_sant_form_ayuda"] = inst_sant_form_ayuda
				context["inst_elect_form_ayuda"] = inst_elect_form_ayuda
				context["muros_paredes_form_ayuda"] = muros_paredes_form_ayuda
				context["techos_posicion_ayuda"] = posiciones_de_ayuda(techo_form_ayuda)
				context["inst_sant_posicion_ayuda"] = posiciones_de_ayuda(inst_sant_form_ayuda)
				context["inst_elect_posicion_ayuda"] = posiciones_de_ayuda(inst_elect_form_ayuda)
				context["mp_posicion_ayuda"] = posiciones_de_ayuda(muros_paredes_form_ayuda)
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
			for un in post:
				if un.endswith("techo_numero_unidad_medida"):
					techo_unidades = int(post[un])
			for pun in post:
				if pun.endswith("techo_precio_unitario"):
					techo_precio_unitario = int(post[pun])
			techo_total = techo_unidades*techo_precio_unitario
			for pt in post:
				if pt.endswith("techo_precio_total_referencial"):
					post[pt] = int(techo_total)
			tch = TechoFormSet(post,request.FILES,instance=obj)
			if tch.is_valid():
				tch.save()
				tch_save = True
			else:
				tch_save = False
				context["techo_form"] = tch
		else:
			tch_save = False

		inst_sant = post.get("inst_sant",False)
		if inst_sant:
			context["inst_sant"] = inst_sant
			for un in post:
				if un.endswith("inst_sant_numero_unidad_medida"):
					inst_sant_unidades = int(post[un])
			for pun in post:
				if pun.endswith("inst_sant_precio_unitario"):
					inst_sant_precio_unitario = int(post[pun])
			inst_sant_total = inst_sant_unidades*inst_sant_precio_unitario
			for pt in post:
				if pt.endswith("inst_sant_precio_total_referencial"):
					post[pt] = int(inst_sant_total)
			inst = InstalacionSanitariaFormSet(post,request.FILES,instance=obj)
			if inst.is_valid():
				inst.save()
				inst_save = True
			else:
				inst_save = False
				context["inst_sant_form"] = inst
		else:
			inst_save = False
	
		inst_elect = post.get("inst_elect",False)
		if inst_elect:
			context["inst_elect"] = inst_elect
			for un in post:
				if un.endswith("inst_elect_numero_unidad_medida"):
					inst_elect_unidades = int(post[un])
			for pun in post:
				if pun.endswith("inst_elect_precio_unitario"):
					inst_elect_precio_unitario = int(post[pun])
			inst_elect_total = inst_elect_unidades*inst_elect_precio_unitario
			for pt in post:
				if pt.endswith("inst_elect_precio_total_referencial"):
					post[pt] = int(inst_elect_total)
			inel = InstalacionElectricaFormSet(post,request.FILES,instance=obj)
			if inel.is_valid():
				inel.save()
				inel_save = True
			else:
				inel_save = False
				context["inst_elect_form"] = inel
		else:
			inel_save = False

		muros_paredes = post.get("muros_paredes",False)
		if muros_paredes:
			context["muros_paredes"] = muros_paredes
			for un in post:
				if un.endswith("mp_numero_unidad_medida"):
					mp_unidades = int(post[un])
			for pun in post:
				if pun.endswith("mp_precio_unitario"):
					mp_precio_unitario = int(post[pun])
			mp_total = mp_unidades*mp_precio_unitario
			for pt in post:
				if pt.endswith("mp_precio_total_referencial"):
					post[pt] = int(mp_total)
			mp = MurosParedesFormSet(post,request.FILES,instance=obj)
			if mp.is_valid():
				mp.save()
				mp_save = True
			else:
				mp_save = False
				context["muros_paredes_form"] = mp
		else:
			mp_save = False

		if tch_save or inst_save or inel_save or mp_save:
			return render(request,"levantamiento/metrado_y_presupuesto.html",context)
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
