# Generated by Django 4.1 on 2024-03-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_channel_descr_alter_epg_descr'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='logo_file',
            field=models.ImageField(blank=True, upload_to='web/logos', verbose_name='台标'),
        ),
    ]