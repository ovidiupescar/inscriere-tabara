# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriere_explo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervare',
            name='notificare_expirare',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='rezervare',
            name='notificare_plata',
            field=models.BooleanField(default='False'),
        ),
    ]
