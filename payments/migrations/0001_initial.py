# Generated by Django 4.0.1 on 2022-07-31 08:50

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0007_remove_order_items_order_cart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=7, verbose_name='amount')),
                ('status', models.CharField(choices=[('unpaid', 'unpaid'), ('inprogress', 'inprogress'), ('paid', 'paid'), ('error', 'error')], default='inprogress', max_length=32, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='createdAt')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='order.order_detail')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='OnlinePayment',
            fields=[
                ('payment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payments.payment')),
                ('variant', models.CharField(choices=[('esewa', 'esewa')], default='esewa', max_length=32, verbose_name='variant')),
                ('tax_amount', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=5, verbose_name='tax_amount')),
                ('service_charge', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=5, verbose_name='service_charge')),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=5, verbose_name='delivery_charge')),
                ('merchant_code', models.CharField(max_length=32, verbose_name='scd')),
                ('transaction_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='txcode')),
                ('product_code', models.CharField(max_length=128, verbose_name='pid')),
                ('extra_content', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'verbose_name': 'OnlinePayment',
                'verbose_name_plural': 'OnlinePayments',
            },
            bases=('payments.payment',),
        ),
    ]
