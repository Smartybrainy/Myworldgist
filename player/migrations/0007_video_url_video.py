# Generated by Django 3.0.5 on 2020-07-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_music_audio_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url_video',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
    ]