# Generated by Django 3.0.5 on 2020-06-29 03:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200618_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 29, 3, 39, 49, 871401, tzinfo=utc)),
        ),
    ]