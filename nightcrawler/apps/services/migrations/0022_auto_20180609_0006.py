# Generated by Django 2.0.5 on 2018-06-09 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_collecteddata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collecteddata',
            options={},
        ),
        migrations.RemoveField(
            model_name='collecteddata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='collecteddata',
            name='num_news',
        ),
        migrations.RemoveField(
            model_name='collecteddata',
            name='toCheck',
        ),
        migrations.RemoveField(
            model_name='collecteddata',
            name='toCountry',
        ),
        migrations.RemoveField(
            model_name='collecteddata',
            name='toID',
        ),
    ]
