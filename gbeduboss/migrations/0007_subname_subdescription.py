# Generated by Django 4.1.1 on 2022-09-25 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gbeduboss', '0006_delete_subdescription_delete_subname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subdescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('one', models.BooleanField()),
                ('two', models.BooleanField()),
                ('three', models.BooleanField()),
                ('four', models.BooleanField()),
                ('five', models.BooleanField()),
                ('six', models.BooleanField()),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gbeduboss.subname')),
            ],
            options={
                'verbose_name': 'Subdescription',
                'verbose_name_plural': 'Subdescriptions',
                'db_table': 'subdescription',
                'managed': True,
            },
        ),
    ]
