from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from utilidades.views import *
from web.models import *

# Create your views here.


def index_video(request):
    context = {}
    return render(request, 'index.html', context)


def inicio(request):
    context = {'message': 'hola'}
    return render(request, 'inicio.html', context)


def contacto(request):
    context = {}
    return render(request, 'contacto.html', context)

def obras(request):
    context = {}
    return render(request, 'obras.html', context)

def escuela(request):
    context = {}
    return render(request, 'escuela.html', context)

def yotambien(request):
    context = {}
    return render(request, 'yo_tambien.html', context)

def coloquios(request):
    context = {}
    return render(request, 'coloquios.html', context)

def malentendido(request):
    context = {}
    return render(request, 'elmalentendido.html', context)

def brujas(request):
    context = {}
    return render(request, 'lasbrujas.html', context)

def silencio(request):
    context = {}
    return render(request, 'silencio.html', context)

def direcciones(request):
    context = {}
    return render(request, 'direcciones.html', context)

def lagaviota(request):
    context = {}
    return render(request, 'lagaviota.html', context)

def compania(request):
    context = {}
    return render(request, 'compania.html', context)

def bellcross(request):
    context = {}
    return render(request, 'bellcross.html', context)

def admision(request):
    context = {}
    return render(request, 'admision.html', context)

def registrar(request):
    try:

        status = True
        message = 'Evio de correo'
        error   = 'Envio de correo exitoso'

        contacto = Contacto()
        contacto.origen   = 2
        contacto.nombre   = request.POST.get('a-nombre') +' '+ request.POST.get('a-apellido')
        contacto.correo   = request.POST.get('a-email')
        contacto.telefono = request.POST.get('a-telefono')
        contacto.save()

        enviar_mail(
            html = True,
            to_email = ['admision@teatroescuela.cl'],
            subject = 'Nueva Consulta',
            message = 'mail/nuevo-admin.html',
            data = {
                'nombre'   : request.POST.get('a-nombre'),
                'apellido' : request.POST.get('a-apellido'),
                'email'    : request.POST.get('a-email'),
                'telefono' : request.POST.get('a-telefono'),
                'run'      : request.POST.get('a-run'),
                'modalidad': request.POST.get('a-modalidad'),
                'mensaje'  : request.POST.get('a-mensaje'),

            },
        )

        return JsonResponse({
            'status'  : status,
            'message' : message,
            'error'   : error
        })

    except Exception as e:

        return JsonResponse({
            'status'  : status,
            'message' : message,
            'error'   : str(e)
        }, status = 500)

def enviar_malla(request):
    try:
        status = True
        message = 'Evio de correo'
        error   = 'Envio de correo exitoso'

        contacto = Contacto()
        contacto.origen   = 1
        contacto.nombre   = request.POST.get('m-nombre')
        contacto.correo   = request.POST.get('m-email')
        contacto.telefono = request.POST.get('m-fono')
        contacto.save()

        enviar_mail(
            html = True,
            to_email = [request.POST.get('m-email')],
            subject = 'ADMISION 2020: Malla Curricular Teatro Escuela',
            message = 'mail/malla-2020.html',
            attach  = 'static/images/malla_2020.png',
        )

        return JsonResponse({
            'status'  : status,
            'message' : message,
            'error'   : error
        })

    except Exception as e:

        return JsonResponse({
            'status'  : status,
            'message' : message,
            'error'   : str(e)
        }, status = 500)
