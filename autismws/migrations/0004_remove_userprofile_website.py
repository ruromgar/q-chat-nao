# Generated by Django 2.0.6 on 2018-10-10 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autismws', '0003_auto_20181010_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
