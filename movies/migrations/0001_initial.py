# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50)),
                ('movie_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=500)),
                ('logo', models.FileField(upload_to='')),
            ],
        ),
    ]
