# Generated by Django 3.0.2 on 2020-01-03 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='content',
        ),
    ]
