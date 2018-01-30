# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pizzashopapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0005_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='China',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=pizzashopapp.models.get_china_upload_path)),
                ('price', models.IntegerField(default=0)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.PizzaShop')),
            ],
        ),
        migrations.CreateModel(
            name='Kavkaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=pizzashopapp.models.get_kavkaz_upload_path)),
                ('price', models.IntegerField(default=0)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.PizzaShop')),
            ],
        ),
        migrations.CreateModel(
            name='Russia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=pizzashopapp.models.get_russia_upload_path)),
                ('price', models.IntegerField(default=0)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.PizzaShop')),
            ],
        ),
    ]
