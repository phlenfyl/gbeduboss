# Generated by Django 4.1.1 on 2022-10-17 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0008_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beats',
            name='album_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beats.album'),
        ),
    ]