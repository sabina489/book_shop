# Generated by Django 4.0.1 on 2022-07-27 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_cart_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]