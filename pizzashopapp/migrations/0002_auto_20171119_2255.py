# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pizza_images')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='logo',
            field=models.ImageField(upload_to='pizzashop_logo/'),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pizzashop',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizzashop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.PizzaShop'),
        ),
    ]
