# Generated by Django 4.1.1 on 2022-09-27 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0003_album_album_beats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album_beats',
            name='album_name',
        ),
        migrations.RemoveField(
            model_name='album_beats',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Album_beats',
        ),
    ]
