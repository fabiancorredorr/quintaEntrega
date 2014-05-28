from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from project.models import Proyecto, Tarea
import datetime
from datetime import date, time, timedelta
from pytz import timezone
import pytz
from django.utils.timezone import utc

# Create your views here.o
def index(request):
    return render_to_response('index.html')
        
def ingresar(request):
    return render(request, 'ingresar.html')

def proyecto(request):
    return render_to_response('proyecto.html')        
@login_required
def crear_proyecto(request):
    return render(request, 'crearProyecto.html')
@login_required
def nuevo_proyecto(request):
    proyecto=Proyecto(nombre_proyecto=request.POST['nombre'], tiempo_Inicio = datetime.date.today(), tiempo_fin = datetime.date.today())
    proyecto.save()
    return HttpResponseRedirect(reverse('project:verProyecto', args=(proyecto.id,)))
@login_required
def mostrarProyectoCreado(request, proyecto_id):
    proyecto=get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'mostrarProyecto.html', {'proyecto':proyecto})    

@login_required
def mis_proyectos(request):
    lista_proyectos=Proyecto.objects.all()
    context={'lista_proyectos':lista_proyectos}
    return render(request, 'mis_proyectos.html', context)

@login_required
def detalle(request, proyecto_id):
    lista_tareas=Tarea.objects.filter(proyecto=proyecto_id)
    context={'lista_tareas':lista_tareas, 'proyecto_id': proyecto_id}
    return render(request, 'mostrarTareas.html', context)

#@permission_required('polls.can_vote', login_url="/login/")
#@permission_required('Proyecto.empezar_tarea')
def inicio(request, tarea_id):
    tarea=get_object_or_404(Tarea, id=tarea_id)
    tarea.tiempo_Inicio= datetime.datetime.utcnow().replace(tzinfo=utc)
    tarea.tiempo_fin=None
    tarea.save()
    messages.info(request, 'Inicio el proyecto correctamente.')
    context={'tiempo_Inicio':tarea.tiempo_Inicio,  'proyecto_id': tarea.proyecto.id}
    return render(request, 'iniciada.html', context)

def fin(request, tarea_id):
    tarea=get_object_or_404(Tarea, id=tarea_id)
    tarea.tiempo_fin= datetime.datetime.utcnow().replace(tzinfo=utc)
    proyecto=get_object_or_404(Proyecto, id=tarea.proyecto.id)
    dif = tarea.tiempo_fin - tarea.tiempo_Inicio
    minutos = (dif.days*24*60) + (dif.seconds/60)
    tarea.acumulado_tarea = tarea.acumulado_tarea + minutos
    proyecto.acumulado_proyecto = proyecto.acumulado_proyecto + minutos
    inicio=tarea.tiempo_Inicio
    final=tarea.tiempo_fin
    tarea.tiempo_fin=None
    tarea.tiempo_Inicio=None
    tarea.save()
    proyecto.save()
    context={'tiempo_fin':final, 'tiempo_inicio':inicio, 'parcial': minutos,  'acumulado':tarea.acumulado_tarea, 'proyecto_id': tarea.proyecto.id}
    return render(request, 'fin.html', context)


def nueva_tarea(request, proyecto_id):
    proyecto=get_object_or_404(Proyecto, id=proyecto_id)
    tarea=Tarea(nombre_tarea=request.POST['nombreTarea'], proyecto=proyecto)
    tarea.save()
    return HttpResponseRedirect(reverse('project:mis_proyectos'))

def validar(request):
    username = request.POST['nombre']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'autenticado.html')
        else:
            return render(request, 'inactivo.html')
    else:
        return render(request, 'error.html')

def salio(request):
    logout(request)
    return render(request, 'salio.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('project:nuevo_proyecto')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })
