# Generated by Django 4.2.2 on 2023-11-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_alter_capitulo_enlace_alter_capitulo_portada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='enlace',
            field=models.URLField(max_length=500, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='portada',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='enlace',
            field=models.URLField(max_length=500, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='enlace',
            field=models.URLField(max_length=500, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='portada',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Portada'),
        ),
    ]