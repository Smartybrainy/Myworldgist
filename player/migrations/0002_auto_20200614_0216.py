# Generated by Django 3.0.5 on 2020-06-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': 'List of videos'},
        ),
        migrations.AlterField(
            model_name='video',
            name='time_added',
            field=models.DateTimeField(),
        ),
    ]