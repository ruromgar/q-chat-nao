# Generated by Django 2.0.6 on 2018-08-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0011_auto_20180822_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity02',
            old_name='first_word',
            new_name='patient_first_word',
        ),
        migrations.RemoveField(
            model_name='activity02',
            name='second_word',
        ),
        migrations.AddField(
            model_name='activity02',
            name='patient_second_word',
            field=models.TextField(blank=True),
        ),
    ]
