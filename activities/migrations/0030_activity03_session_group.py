# Generated by Django 2.0.6 on 2018-12-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0029_activity02_failed_second_word_reaction_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity03',
            name='session_group',
            field=models.IntegerField(null=True),
        ),
    ]
