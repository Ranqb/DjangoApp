# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0003_auto_20171210_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sushi',
            old_name='shop',
            new_name='pizzashop',
        ),
    ]
