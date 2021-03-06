# Generated by Django 2.0.6 on 2019-07-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autismws', '0009_auto_20190714_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tea',
            field=models.NullBooleanField(verbose_name='¿Presenta el paciente signos de TEA?'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default='12', verbose_name='Edad (en meses)'),
        ),
    ]
