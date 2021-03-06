# Generated by Django 4.0.1 on 2022-07-31 10:50

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_cart_total_alter_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=5, verbose_name='quantity'),
        ),
    ]
