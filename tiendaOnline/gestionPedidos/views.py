from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from tiendaOnline.settings import EMAIL_HOST_USER


# Create your views here.


def busquedaProductos(request):
    return render(request, "formulario.html")


def buscar(request):
    producto = request.GET["producto"]
    if producto and len(producto) <= 20:
        mensaje = f"Articulo buscado: {request.GET['producto']}"

        articulos = Articulos.objects.filter(
            nombre__icontains=producto
        )  # select * from Articulos like nombre= var producto
        return render(
            request,
            "resultados_busqueda.html",
            {
                "articulos": articulos,
                "query": producto,
            },
        )
    else:
        mensaje = "producto no encontrado o muy largo"
        return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":
        subject = request.POST["asunto-contacto"]
        message = (
            request.POST["mensaje-contacto"] + " : " + request.POST["correo-contacto"]
        )
        email_from = EMAIL_HOST_USER
        recipient_list = [
            "julioasmb@gmail.com",
        ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        send_mail(
            "confirmacion solicitud",
            "sulicitud ingresada con exito",
            email_from,
            [request.POST["correo-contacto"]],
            fail_silently=False,
        )
        return render(request, "gracias.html")
    else:
        return render(request, "contacto.html")
