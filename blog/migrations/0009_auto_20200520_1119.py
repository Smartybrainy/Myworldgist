# Generated by Django 3.0.5 on 2020-05-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200514_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='added_date',
            field=models.DateTimeField(),
        ),
    ]
