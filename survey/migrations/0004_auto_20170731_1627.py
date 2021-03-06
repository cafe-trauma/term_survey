# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20170728_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='header',
            field=models.CharField(default='Default Header', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='logo',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='welcome_message',
            field=models.TextField(blank=True),
        ),
    ]
