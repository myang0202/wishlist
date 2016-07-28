# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=155)),
                ('username', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default='')),
            ],
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
