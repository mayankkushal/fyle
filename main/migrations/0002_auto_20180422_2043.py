# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='id',
        ),
        migrations.AlterField(
            model_name='branch',
            name='ifsc',
            field=models.CharField(editable=False, max_length=11, primary_key=True, serialize=False),
        ),
    ]
