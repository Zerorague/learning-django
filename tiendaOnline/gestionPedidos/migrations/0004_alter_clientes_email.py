# Generated by Django 4.2.3 on 2023-08-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestionPedidos", "0003_alter_clientes_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientes",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Correo"
            ),
        ),
    ]
