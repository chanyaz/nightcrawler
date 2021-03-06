# Generated by Django 2.0.6 on 2018-06-20 23:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0033_auto_20180617_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collecteddata',
            name='avgcompound',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='newsdata',
            name='date',
            field=models.DateField(blank=True, db_index=True, default=django.utils.timezone.now, null=True),
        ),
    ]
