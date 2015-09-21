from django.shortcuts import render,redirect
from django.http import JsonResponse
from ayudas.models import Ayuda
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
	# if request.user.is_superuser:
	ayudas = []
	form = ""
	for ayuda in Ayuda.objects.all().order_by("form"):
		if form != ayuda.form:
			url = ayuda.form
			txt = ayuda.form.replace("_"," ")
			ayudas.append([url,txt])
		form = ayuda.form
	context = {"next": request.path,"ayudas": ayudas}
	return render(request,"ayudas/index.html",context)
	# return redirect("/")

# @login_required
def edit(request,form):
	# if request.user.is_superuser:
	ayudas = Ayuda.objects.filter(form=form).order_by("id")
	context = {"next": request.path,"ayudas": ayudas,"form": form}
	return render(request,"ayudas/edit.html",context)
	# return redirect("/")

# @login_required
def show(request,form,posicion):
	ayuda = Ayuda.objects.get(form=form,posicion=posicion)
	context = {"next": request.path,"ayuda": ayuda}
	return render(request,"ayudas/show.html",context)

# @login_required
def create(request,form):
	# if request.user.is_superuser:
	ayuda = Ayuda.objects.create(form=form,posicion=0,title="",text="")
	ayuda = {"id": ayuda.id,"posicion": ayuda.posicion,"title": ayuda.title,"text":ayuda.text}
	return JsonResponse({"ayuda": ayuda})
	# return redirect("/")

# @login_required
def update(request,form):
	# if request.user.is_superuser:
	post = request.POST
	ayudas = Ayuda.objects.filter(form=form)
	for ayuda in ayudas:
		id = ayuda.id
		if "title["+str(id)+"]" in post:
			posicion = post["posicion["+str(id)+"]"]
			title = post["title["+str(id)+"]"]
			text = post["text["+str(id)+"]"]
			ayuda.posicion = posicion
			ayuda.title = title
			ayuda.text = text
			ayuda.save()

	return JsonResponse({})
	# return redirect("/")