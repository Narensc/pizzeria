# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4)),
        ),
    ]