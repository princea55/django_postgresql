# Generated by Django 3.1.1 on 2020-09-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0003_auto_20200901_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField()),
                ('date', models.DateField()),
                ('symbol', models.CharField(max_length=50)),
                ('opens', models.IntegerField()),
                ('close', models.IntegerField()),
                ('low', models.IntegerField()),
                ('high', models.IntegerField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
