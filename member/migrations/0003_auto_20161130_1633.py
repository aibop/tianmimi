# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20161130_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], max_length=16, verbose_name='性别'),
        ),
    ]