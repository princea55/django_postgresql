# Generated by Django 3.1.1 on 2020-09-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0004_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='high',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='low',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='opens',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.FloatField(),
        ),
    ]
