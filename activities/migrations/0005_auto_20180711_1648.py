# Generated by Django 2.0.6 on 2018-07-11 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0004_auto_20180703_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='content/files/activity_01', verbose_name='File')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('sentence', models.TextField()),
                ('transcription', models.TextField()),
                ('extra_data', models.TextField()),
                ('session', models.IntegerField()),
                ('session_group', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Audiofl',
        ),
    ]
