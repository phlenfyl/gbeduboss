# Generated by Django 4.1.1 on 2022-12-09 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0022_beats_display'),
    ]

    operations = [
        migrations.DeleteModel(
            name='All_artist',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='category',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='beats',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='beats',
            name='category',
        ),
        migrations.RemoveField(
            model_name='beats',
            name='genre',
        ),
    ]
