# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0003_remove_usuario_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
