# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('doing', 'Doing'), ('done', 'Done')], max_length=5),
        ),
    ]
