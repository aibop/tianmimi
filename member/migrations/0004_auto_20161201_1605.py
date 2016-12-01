# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20161130_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='access_token',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='expires_in',
            field=models.BigIntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='member',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=128, unique=True, verbose_name='会员名字'),
        ),
    ]
