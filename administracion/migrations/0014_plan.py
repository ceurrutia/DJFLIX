# Generated by Django 4.2.2 on 2023-11-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0013_alter_suscriptor_password1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(max_length=100, unique=True, verbose_name='Nombre plan')),
            ],
            options={
                'verbose_name_plural': 'Planes',
            },
        ),
    ]
