# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='be_attentioner', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attentioner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '关注列表',
            },
        ),
        migrations.AlterUniqueTogether(
            name='attention',
            unique_together=set([('user', 'follow_user')]),
        ),
    ]
