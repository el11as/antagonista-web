from django.shortcuts import render

# Create your views here.


def index_video(request):
    context = {}
    return render(request, 'index.html', context)


def inicio(request):
    context = {'message': 'hola'}
    return render(request, 'inicio.html', context)


def contacto(request):
    context = {}
    print('Estoy en contacto')
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
