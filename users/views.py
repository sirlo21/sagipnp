#-*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.models import User
# from users.models import Account
from django.contrib.auth.decorators import login_required

# @login_required
# def index(request):
# 	if request.user.is_superuser:
# 		users = User.objects.all()
# 		context = {"next": request.path,"users": users}
# 		return render(request,"users/index.html",context)
# 	return redirect("/")

# @login_required
# def create(request):
# 	if request.user.is_superuser:
# 		if request.method == "POST":
# 			post = request.POST
# 			context = {"next": request.path,"form": options(post)}
# 			fields = valid_user(post)
# 			if fields:
# 				username = fields["username"]
# 				name = fields["name"]
# 				lastname = fields["lastname"]
# 				email = fields["email"]
# 				password = fields["password"]
# 				grado = fields["grado"]
# 				unidad = fields["unidad"]
# 				if post["type"].lower() == "usuario":
# 					us = User.objects.create_user(username=username,first_name=name,last_name=lastname,email=email,password=password)
# 					if not(grado is None and unidad is None):
# 						Account.objects.create(grado=grado,unidad=unidad,user=us)
# 					return redirect("/users/")
# 				elif post["type"].lower() == "superuser":
# 					sus = User.objects.create_superuser(username=username,first_name=name,last_name=lastname,email=email,password=password)
# 					if not(grado is None and unidad is None):
# 						Account.create(grado=grado,unidad=unidad,user=sus)
# 					return redirect("/users/")
# 		else:
# 			if request.is_ajax():
# 				grado = request.GET.get("grado",False)
# 				if grado:
# 					if grado in options()["rango"]:
# 						return JsonResponse({"unidades": options()["unidades"]})
# 			context = {"next": request.path,"form": options()}
# 		return render(request,"users/crear_usuario.html",context)
# 	return redirect("/")

# @login_required
# def edit(request,id):
# 	if request.user.is_superuser:
# 		id = int(id)
# 		if User.objects.filter(id=id):
# 			if request.method == "POST":
# 				post = request.POST
# 				context = {"next": request.path,"form": options(post),"id": id}
# 				fields = valid_user(post,False,id)
# 				if fields:
# 					username = fields["username"]
# 					name = fields["name"]
# 					lastname = fields["lastname"]
# 					email = fields["email"]
# 					password = fields["password"]
# 					grado = fields["grado"]
# 					unidad = fields["unidad"]
# 					us = User.objects.get(id=id)
# 					us.username = username
# 					us.lastname = lastname
# 					if post["type"].lower() == "usuario":
# 						us.is_superuser = False
# 					elif post["type"].lower() == "superuser":
# 						us.is_superuser = True
# 					us.email = email
# 					if password is not None:
# 						us.set_password(password)
# 					if not(grado is None and unidad is None):
# 						if hasattr(us,"account"):
# 							act = us.account
# 							act.grado = grado
# 							act.unidad = unidad
# 							act.save()
# 						else:
# 							Account.objects.create(grado=grado,unidad=unidad,user=us)
# 					else:
# 						if hasattr(us,"account"):
# 							us.account.delete()
# 					us.save()
# 					return redirect("/users/")
# 			else:
# 				if request.is_ajax():
# 					grado = request.GET.get("grado",False)
# 					if grado:
# 						if grado in options()["rango"]:
# 							return JsonResponse({"unidades": options()["unidades"]})
# 				user = User.objects.get(id=id)
# 				dates = {"username": user.username,"name": user.first_name ,"lastname": user.last_name,"email": user.email,	
# 					"password": "","password_confirm": ""
# 				}
# 				if user.is_superuser:
# 					dates.update(type="superuser")
# 				else:
# 					dates.update(type="usuario")
# 				if hasattr(user,"account"):
# 					dates.update(grado=user.account.grado,unidad=user.account.unidad)
# 				context = {"next": request.path,"form": options(dates,id),"id": id}
# 			return render(request,"users/editar_usuario.html",context)
# 		return redirect("/users/")
# 	return redirect("/")

# @login_required
# def delete(request,id):
# 	if request.user.is_superuser:
# 		context = {}
# 		if User.objects.filter(id=id):
# 			user = User.objects.get(id=id)
# 			context = {"id": user.id}
# 			user.delete()
# 		return JsonResponse(context)
# 	return redirect("/")

def log_out(request):
	if request.user.is_authenticated():
		logout(request)
		next = request.GET.get("next","/")
		return redirect(next)
	return redirect("/")
