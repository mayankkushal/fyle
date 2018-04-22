# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('discrict', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Bank')),
            ],
        ),
    ]
