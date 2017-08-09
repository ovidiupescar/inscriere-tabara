# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=60)),
                ('data_nasterii', models.DateTimeField(verbose_name='data nasterii')),
                ('sex', models.CharField(max_length=1)),
                ('tip', models.CharField(max_length=20)),
                ('cort', models.BooleanField()),
                ('cladire', models.CharField(max_length=1)),
                ('camera', models.CharField(max_length=2)),
                ('pat', models.CharField(max_length=2)),
                ('comunitate', models.CharField(max_length=60)),
                ('grupa', models.CharField(max_length=60)),
                ('probleme', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rezervare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar_rezervare', models.CharField(max_length=10)),
                ('nume', models.CharField(max_length=60)),
                ('tip', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=20)),
                ('data_rezervarii', models.DateTimeField(verbose_name='data rezervarii')),
                ('data_modificare', models.DateTimeField(auto_now=True)),
                ('data_expirarii', models.DateTimeField(verbose_name='data expirarii')),
                ('notificare_plata', models.BooleanField()),
                ('notificare_expirare', models.BooleanField()),
                ('platit', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='rezervare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscriere_explo.Rezervare'),
        ),
    ]
