from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render


class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def getNombre(self):
        return self.__nombre

    @property
    def getApellido(self):
        return self.__apellido


def Prueba(request):
    persona2 = Persona("Julio", "San Martin")
    doc_externo = loader.get_template("plt.html")
    diccionario_exContexto = {
        "nombre": persona2.getNombre,
        "apellido": persona2.getApellido,
        "temas": [
            "Plantillas",
            "Modelos",
            "Formularios",
            "Vistas",
            "Despliegue aplicacion",
        ],
    }
    documento = doc_externo.render(diccionario_exContexto)
    return HttpResponse(documento)


def Shortcut(request):
    persona3 = Persona("Natalia", "BUstos")
    diccionario_exContexto = {
        "nombre": persona3.getNombre,
        "apellido": persona3.getApellido,
        "temas": [
            "Plantillas",
            "Modelos",
            "Formularios",
            "Vistas",
            "Despliegue aplicacion",
        ],
    }
    return render(request, "plt.html", diccionario_exContexto)


def barraNavegacion(request):
    persona4 = Persona("Javiera", "FLORES")

    diccionario_exContexto = {
        "nombre": persona4.getNombre,
        "apellido": persona4.getApellido,
        "temas": [
            "Plantillas",
            "Modelos",
            "Formularios",
            "Vistas",
            "Despliegue aplicacion",
        ],
    }

    return render(request, "barra.html", diccionario_exContexto)


def herencias(request):
    diccionario = {
        "temas": [
            "variables",
            "poo",
            "primera app",
        ],
    }

    return render(request, "cursoC.html", diccionario)


def cursoPythonHerencia(request):
    return render(request, "cursoPython.html", {})
