# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='会员名字')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='年龄')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=2, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=128, verbose_name='电话号码')),
                ('portrait', models.ImageField(blank=True, null=True, upload_to='member_img/')),
                ('login_ip', models.GenericIPAddressField()),
                ('register_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='注册时间')),
                ('last_login_time', models.DateTimeField(auto_now=True, null=True, verbose_name='登录时间')),
            ],
            options={
                'verbose_name_plural': 'Member',
                'verbose_name': 'Member',
            },
        ),
    ]
