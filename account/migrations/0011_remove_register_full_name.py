# Generated by Django 4.0.1 on 2022-07-15 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_register_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='full_name',
        ),
    ]
