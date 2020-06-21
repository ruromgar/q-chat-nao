# Generated by Django 2.0.6 on 2019-07-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autismws', '0010_auto_20190716_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='added_to_dataset',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tea',
            field=models.NullBooleanField(help_text='Este campo se completa de forma automática en función de las respuestas del usuario. Cambiar solo si se considera que el algoritmo está equivocado.', verbose_name='¿Presenta el paciente signos de TEA?'),
        ),
    ]