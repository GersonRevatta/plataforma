# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0007_auto_20170106_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]
