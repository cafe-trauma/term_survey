# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondant',
            name='identifier',
        ),
    ]
