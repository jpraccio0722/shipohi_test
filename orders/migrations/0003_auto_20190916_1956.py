# Generated by Django 2.2.5 on 2019-09-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190916_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='warehouse_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.Warehouse'),
        ),
    ]