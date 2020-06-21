# Generated by Django 2.0.6 on 2018-11-06 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0020_auto_20181102_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity07',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.IntegerField()),
                ('session_group', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_act07', to=settings.AUTH_USER_MODEL)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_act07', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]