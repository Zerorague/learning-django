from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(
        max_length=30,
    )
    direccion = models.CharField(
        max_length=50,
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Correo")
    telefono = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nombre


class Articulos(models.Model):
    nombre = models.CharField(
        max_length=30,
    )
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return (
            f"nombre: {self.nombre}\nseccion: {self.seccion}\nprecio: {self.precio}\n"
        )


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estaEntregado = models.BooleanField()
