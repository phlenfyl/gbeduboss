# Generated by Django 4.1.1 on 2022-10-15 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0005_album_album_beats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number_beat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_beats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats.beats')),
            ],
        ),
    ]
