# -*- coding: utf-8 -*-

# Generated by Django 2.0.5 on 2018-06-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_newsdata_compound'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsdata',
            name='freqList',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='newsdata',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
