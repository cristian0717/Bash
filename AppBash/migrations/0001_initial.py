# Generated by Django 4.0.4 on 2022-06-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=40)),
                ('rubro', models.CharField(max_length=15)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('dni', models.IntegerField()),
                ('tipo_de_factura', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=15)),
                ('contraseña', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MediosDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjeta', models.IntegerField()),
                ('mercado_pago', models.IntegerField()),
                ('efectivo', models.IntegerField()),
                ('transferencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('numero_vendedor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=20)),
                ('codigo', models.CharField(max_length=15)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
