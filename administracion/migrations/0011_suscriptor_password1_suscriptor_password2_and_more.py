# Generated by Django 4.2.2 on 2023-11-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0010_remove_pelicula_categoria_remove_serie_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscriptor',
            name='password1',
            field=models.CharField(default=1234, verbose_name='password1'),
        ),
        migrations.AddField(
            model_name='suscriptor',
            name='password2',
            field=models.CharField(default=1234, verbose_name='password2'),
        ),
        migrations.AddField(
            model_name='suscriptor',
            name='username',
            field=models.CharField(default='suscriptor', verbose_name='username'),
        ),
    ]
