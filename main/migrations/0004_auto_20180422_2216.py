# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180422_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='discrict',
            new_name='district',
        ),
    ]
