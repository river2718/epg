# Generated by Django 4.1 on 2024-03-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_alter_channel_descr_alter_epg_descr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='descr',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='epg',
            name='descr',
            field=models.TextField(blank=True, default='', verbose_name='节目描述'),
        ),
    ]