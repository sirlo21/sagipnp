from ayudas.models import Ayuda

def posiciones_de_ayuda(form_ayuda):
	posicion_ayuda = []
	for ayuda in Ayuda.objects.filter(form=form_ayuda):
		posicion_ayuda.append(ayuda.posicion)
	return posicion_ayuda
