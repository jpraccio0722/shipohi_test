# Generated by Django 2.2.5 on 2019-09-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
