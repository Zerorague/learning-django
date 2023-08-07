from django.http import HttpResponse
import datetime
from django.template import Template, Context
from time import sleep
from django.template import loader


class Persona(object):
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


def saludo(
    request,
):  # cada funcion es una vista que devuelve una respuesta, en este caso el texto
    documento = """
    <html>
        <body>
            <h1>Hola Mundo, esta es mi primera pagina con django</h1>
        </body>
    </html>

    """
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Hasta luego")


def dameFecha(request):
    documento = f"""
    <html>
        <body>
            <h1>↓La fecha y hora actual son↓ <br>
            {datetime.datetime.now()}</h1>
        </body>
    </html>

    """
    return HttpResponse(documento)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def ageCalculator(request, age, edadActual):
    periodo = age - 2023
    edadFutura = edadActual + periodo
    documento = f"<html><body><h2>en el año {age} tendras {edadFutura} años/ el factorial de {edadActual} es {factorial(edadActual)} </h2></body></html>"
    return HttpResponse(documento)


def plantilla(request):
    persona1 = Persona("Fran", "Valdés")
    nombre = "Julio"
    apellido = "San Martín"
    documentoExterno = open(
        R"C:\Users\julio\Desktop\Curso DJANGO\proyecto1\plantilla.html"
    )
    plantilla = Template(documentoExterno.read())

    documentoExterno.close()

    contexto = Context(
        {
            "nombre_persona": persona1,
            "apellido": persona1.apellido,
            "fecha": datetime.datetime.now,
        }
    )

    documento = plantilla.render(contexto)
    return HttpResponse(documento)  # documento renderizado


def lista_html(request):
    persona2 = Persona("Julio", "San Martín")
    # documento_externo = open(
    #    R"C:\Users\julio\Desktop\Curso DJANGO\proyecto1\plantilla.html"
    # )
    # template = Template(documento_externo.read())
    # documento_externo.close()

    doc_externo = loader.get_template(
        "plt.html"
    )  # ocupamos el loader para cargar la plantilla
    # revisar y modificar settings para dar a conocer la ruta donde estaran las plantillas

    # contexto = Context(
    #     {
    #         "nombre": persona2.nombre,
    #         "apellido": persona2.apellido,
    #         "temas": [
    #             "Plantillas",
    #             "Modelos",
    #             "Formularios",
    #             "Vistas",
    #             "Despliegue aplicacion",
    #         ],
    #     }
    # ) ya no se pasa un contexto al render, sino que directamente el diccionario

    diccionario_exContexto = {
        "nombre": persona2.nombre,
        "apellido": persona2.apellido,
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
