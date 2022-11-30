# Generated by Django 4.0.2 on 2022-11-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_tiempo_fecha_final_alter_tiempo_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo',
            name='fecha_final',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de finalización'),
        ),
        migrations.AlterField(
            model_name='tiempo',
            name='fecha_inicio',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de inicio'),
        ),
    ]
