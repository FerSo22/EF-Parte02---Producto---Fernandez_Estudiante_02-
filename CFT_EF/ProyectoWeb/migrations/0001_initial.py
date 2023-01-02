# Generated by Django 4.1.5 on 2023-01-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=4)),
                ('nombre', models.TextField(max_length=80)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('fecha_compra', models.DateField(auto_now=True)),
                ('facha_registro', models.DateField(auto_now_add=True)),
                ('estado', models.TextField(max_length=1)),
            ],
        ),
    ]