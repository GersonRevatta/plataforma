# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20170106_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='image',
            field=models.ImageField(upload_to='document'),
        ),
    ]
