# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-17 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
