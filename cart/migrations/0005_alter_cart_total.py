# Generated by Django 4.0.1 on 2022-07-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(blank=True, null=True, verbose_name='price'),
        ),
    ]
