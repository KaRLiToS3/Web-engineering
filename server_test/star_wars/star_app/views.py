from django.http import HttpResponse
from django.shortcuts import render
from star_app.models import Faccion

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def listadoDeFacciones(request):
    facciones = Faccion.objects.all()
    names = ", ".join([faccion.nombre for faccion in facciones])
    return HttpResponse(names)

def detalleFaccion(request, faccion_id):
    try:
        faccion = Faccion.objects.get(id=faccion_id)
        personajes = faccion.personajes.all()
        return HttpResponse(f"{faccion.nombre}\n {chr(10).join([personaje.nombre for personaje in personajes])}")
    except Faccion.DoesNotExist:
        return HttpResponse("Facción no encontrada", status=404)
    