# Generated by Django 3.0.2 on 2020-01-04 22:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job_list', '0004_auto_20200103_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 3, 22, 2, 47, 423100, tzinfo=utc)),
        ),
    ]