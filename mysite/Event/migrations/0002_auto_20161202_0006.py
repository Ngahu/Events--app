# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=40)),
                ('Event_type', models.CharField(max_length=300)),
                ('Event_topic', models.CharField(max_length=250)),
                ('Event_image', models.FileField(upload_to=b'')),
                ('Event_description', models.CharField(max_length=1000)),
                ('Organizer_name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Create',
        ),
    ]
