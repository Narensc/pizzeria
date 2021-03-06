# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20170523_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
