from ast import Return
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from AppGimnasio.forms import *
from .models import registro
from django.db.models import Q
# Create your views here.


def Index(request):
    return render(request, 'AppGimnasio/Index.html')

def actividades(request):
    return render(request, 'AppGimnasio/Actividades.html')

def horarios(request):
    return render(request, 'AppGimnasio/Horarios.html')

def contacto(request):
    return render(request, 'AppGimnasio/Contacto.html')

def registro_persona(request):
    form = registroFormulario()
    data = {'form':form}
    if request.method == 'POST':
        miformulario = registroFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            miformulario.save()
            data['mensaje'] = "Datos Resgistrados"
            return render(request, 'AppGimnasio/Index.html')
    else:
        miformulario= registroFormulario()
    return render(request, 'AppGimnasio/Registro.html', data)




def buscarpersona(request):
    return render(request,"AppGimnasio/Busquedadni.html")
    

def buscar(request):
    if request.GET['dni']:
        dni = request.GET['dni']
        dni = registro.objects.filter(dni__icontains=dni)
        return render(request,"AppGimnasio/BusquedaRespuesta.html",{"persona":dni})
    else:
        respuesta = "No se encuentra"
    return render(request, "AppGimnasio/BusquedaRespuesta.html", {"respuesta":respuesta})

