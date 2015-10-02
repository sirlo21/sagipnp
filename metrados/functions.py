# -*- coding: utf-8 -*-

def get_json_metrado(obj):
	metrados = []
	for metrado in obj.all():
		metrados.append({"id": metrado.id,"codigo": metrado.codigo,"descripcion": metrado.descripcion})
	return metrados
