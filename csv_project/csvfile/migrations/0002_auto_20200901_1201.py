# Generated by Django 3.1.1 on 2020-09-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
