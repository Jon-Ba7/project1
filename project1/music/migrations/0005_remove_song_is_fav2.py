# Generated by Django 2.0.5 on 2018-05-23 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_is_fav2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_fav2',
        ),
    ]
