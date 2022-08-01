# Generated by Django 4.0.1 on 2022-07-29 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_bookcategory_image'),
        ('cart', '0009_alter_cartitem_cart'),
        ('order', '0004_order_detail_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_items',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='order_items',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_items',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='cart.cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_price',
            field=models.FloatField(blank=True, null=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
    ]
