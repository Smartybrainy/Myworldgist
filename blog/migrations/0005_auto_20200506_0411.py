# Generated by Django 3.0.5 on 2020-05-06 03:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200502_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 3, 11, 4, 449813, tzinfo=utc)),
        ),
    ]
