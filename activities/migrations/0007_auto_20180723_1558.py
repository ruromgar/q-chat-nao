# Generated by Django 2.0.6 on 2018-07-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20180713_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity01',
            name='point_list',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='activity01',
            name='reaction_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='activity01',
            name='time_list',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='activity01',
            name='total_points',
            field=models.FloatField(null=True),
        ),
    ]
