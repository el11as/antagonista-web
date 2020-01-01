from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from utilidades.views import *

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

        enviar_mail(
            html = True,
            to_email = ['elias.gomezfuentes@gmail.com'],
            subject = 'Nuevo Registro',
            message = 'mail/nuevo-admin.html',
            data = {
                'nombre'   : request.POST.get('a-nombre'),
                'apellido' : request.POST.get('a-apellido'),
                'email'    : request.POST.get('a-email'),
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

        enviar_mail(
            html = True,
            to_email = [request.POST.get('m-email')],
            subject = 'Malla Curricular Antagonista',
            message = 'mail/malla-2020.html',
            attach  = 'static/images/malla-2020.png',
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
