# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20170727_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(max_length=2500),
        ),
    ]
