# Generated by Django 3.0.5 on 2020-07-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_auto_20200710_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='desc',
        ),
        migrations.AddField(
            model_name='video',
            name='disc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='disc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
