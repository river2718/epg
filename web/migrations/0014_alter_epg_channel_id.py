# Generated by Django 4.1 on 2024-03-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_epg_chan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epg',
            name='channel_id',
            field=models.CharField(max_length=50, verbose_name='频道ID'),
        ),
    ]
