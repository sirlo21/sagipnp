from django.shortcuts import render
from levantamiento.models import Levantamiento,RegionPolicial,TComisaria,CComisaria,Especialidad,Category
from reparar.models import Techo,InstalacionSanitaria,InstalacionElectrica,MurosParedes
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required
from levantamiento.functions import posiciones_de_ayuda
from django.http import JsonResponse
from ubigeo.models import Ubigeo
from metrados.models import *
from metrados.forms import *

@login_required
def ficha_tecnica(request,id):
	levantamiento = Levantamiento.objects.get(id=id)
	distrito = levantamiento.ubigeo
	provincia = Ubigeo.objects.get(id=distrito.parent_id)
	departamento = Ubigeo.objects.get(id=provincia.parent_id)
	context = {"obj": levantamiento,"distrito": distrito,"provincia": provincia,"departamento": departamento,
		"form": FichaTecnicaForm()
	}
	return render(request,"metrados/ficha_tecnica.html",context)

def json(request):
	context = {}
	if request.GET.get("metrado1_id",False):
		metrado1_id = request.GET["metrado1_id"]
		context["metrado2"] = []
		for metrado2 in Metrado2.objects.filter(metrado1_id=metrado1_id):
			context["metrado2"].append({"id": metrado2.id,"name": metrado2.codigo})
	elif request.GET.get("metrado2_id",False):
		metrado2_id = request.GET["metrado2_id"]
		context["metrado3"] = []
		for metrado3 in Metrado3.objects.filter(metrado2_id=metrado2_id):
			context["metrado3"].append({"id": metrado3.id,"name": metrado3.codigo})
	elif request.GET.get("metrado3_id",False):
		metrado3_id = request.GET["metrado3_id"]
		context["metrado4"] = []
		for metrado4 in Metrado4.objects.filter(metrado3_id=metrado3_id):
			context["metrado4"].append({"id": metrado4.id,"name": metrado4.codigo})
	return JsonResponse(context)
