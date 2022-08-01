# Generated by Django 4.0.1 on 2022-07-31 10:33

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=Decimal('2.0'), max_digits=5, verbose_name='total'),
        ),
    ]