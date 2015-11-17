from django.shortcuts import render,redirect
from django.http import JsonResponse
from ayudas.models import Ayuda
from ayudas.forms import AyudaFormSet
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	if request.user.is_superuser:
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
	return redirect("/")

@login_required
def edit(request,form):
	if request.user.is_superuser:
		if request.method == "POST":
			ayudas_formset = AyudaFormSet(request.POST,queryset=Ayuda.objects.filter(form=form),prefix="form_ayuda")
			if ayudas_formset.is_valid():
				print ayudas_formset
				ayudas = ayudas_formset.save(commit=False)
				print ayudas
				for ayuda in ayudas:
					ayuda.form = form
					ayuda.save()
		else:
			ayudas_formset = AyudaFormSet(queryset=Ayuda.objects.filter(form=form),prefix="form_ayuda")
		context = {"next": request.path,"ayudas_formset": ayudas_formset,"form": form}
		return render(request,"ayudas/edit.html",context)
	return redirect("/")

@login_required
def show(request,form,posicion):
	ayuda = Ayuda.objects.get(form=form,posicion=posicion)
	context = {"next": request.path,"ayuda": ayuda}
	return render(request,"ayudas/show.html",context)
