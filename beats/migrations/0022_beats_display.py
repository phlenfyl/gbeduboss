# Generated by Django 4.1.1 on 2022-10-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0021_album_price_beats_buy_beats_freedownload_beats_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='beats',
            name='display',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]