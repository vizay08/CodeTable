# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeEditor', '0002_code_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='shared_code',
        ),
        migrations.AddField(
            model_name='code',
            name='is_writable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='language',
            field=models.CharField(default='JAVA', max_length=12),
        ),
    ]