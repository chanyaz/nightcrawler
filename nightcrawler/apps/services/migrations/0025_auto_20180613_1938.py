# Generated by Django 2.0.4 on 2018-06-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_auto_20180609_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='collecteddata',
            name='avgcompound',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='collecteddata',
            name='sumcompound',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]
