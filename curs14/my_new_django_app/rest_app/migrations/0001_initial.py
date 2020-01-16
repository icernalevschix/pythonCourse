# Generated by Django 3.0 on 2020-01-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FancyCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
    ]