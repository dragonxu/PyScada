# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-07 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0051_auto_20181206_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='max_type',
            field=models.CharField(choices=[('gte', '>='), ('gt', '>')], default='gte', max_length=4, verbose_name='value_class'),
        ),
        migrations.AddField(
            model_name='variable',
            name='min_type',
            field=models.CharField(choices=[('lte', '<='), ('lt', '<')], default='lte', max_length=4, verbose_name='value_class'),
        ),
        migrations.AddField(
            model_name='variableproperty',
            name='max_type',
            field=models.CharField(choices=[('gte', '>='), ('gt', '>')], default='gte', max_length=4, verbose_name='value_class'),
        ),
        migrations.AddField(
            model_name='variableproperty',
            name='min_type',
            field=models.CharField(choices=[('lte', '<='), ('lt', '<')], default='lte', max_length=4, verbose_name='value_class'),
        ),
    ]
