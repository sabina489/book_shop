# Generated by Django 4.0.1 on 2022-07-29 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_items_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_items',
            name='order_cart',
        ),
        migrations.AlterField(
            model_name='order_items',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order_detail'),
        ),
    ]
