from django.http import HttpResponse
from django.shortcuts import render
from AppBash.models import Login, Vendedor, Ventas, MediosDePago, Articulo, Cliente
from django.template import loader

def login (request):
    return render (request, "AppBash/login.html")

def vendedor (request):
    return render (request, "AppBash/vendedor.html")


def ventas (request):
    return render (request, "AppBash/ventas.html")



def mediosDePago (request):
    return render (request, "AppBash/mediosdepago.html")


def articulo (request):
    return render (request, "AppBash/articulo.html")



def cliente (request):
    return render (request, "AppBash/cliente.html")



def plantilla1 (self):
    plantilla = loader.get_template("AppBash/inicio.html")
    documento = plantilla.render()
    return HttpResponse (documento)
    