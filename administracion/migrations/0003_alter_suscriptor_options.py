
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_serie_cant_capitulos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suscriptor',
            options={'verbose_name_plural': 'Suscriptores'},
        ),
    ]
