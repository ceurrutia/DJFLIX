# Generated by Django 4.2.5 on 2023-10-26 01:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha_y_hora',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Fecha y hora'),
        ),
    ]
