# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-08 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20160708_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='logo',
            field=models.ImageField(upload_to='Photo/logo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='Photo/item'),
        ),
        migrations.AlterField(
            model_name='servicecontent',
            name='foto_portada',
            field=models.ImageField(upload_to='Photo/service'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='Photo/slider'),
        ),
    ]
