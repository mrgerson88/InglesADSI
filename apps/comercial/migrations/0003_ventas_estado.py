# Generated by Django 3.1 on 2020-09-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0002_detalleventa_ventas'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='estado',
            field=models.CharField(choices=[('cotizacion', 'Cotizacion'), ('venta', 'Venta')], default='cotizacion', max_length=10),
        ),
    ]