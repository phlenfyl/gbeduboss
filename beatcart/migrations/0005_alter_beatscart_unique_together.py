# Generated by Django 4.1.1 on 2022-10-31 11:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beatcart', '0004_alter_beatscart_session_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='beatscart',
            unique_together={('user', 'session_id')},
        ),
    ]
