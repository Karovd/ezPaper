# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0002_auto_20170613_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='telephone',
        ),
    ]
