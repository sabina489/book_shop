# Generated by Django 4.0.1 on 2022-07-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_register_firstname_remove_register_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='full_name'),
        ),
    ]
