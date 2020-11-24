# Generated by Django 3.0.5 on 2020-07-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_auto_20200630_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]