# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-15 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=200)),
                ('book_title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
            ],
        ),
    ]
