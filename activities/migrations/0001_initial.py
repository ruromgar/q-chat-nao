# Generated by Django 2.0.6 on 2018-07-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiofl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('fl', models.FileField(blank=True, null=True, upload_to='audio_uploads', verbose_name='File')),
            ],
        ),
    ]
