# Generated by Django 4.0.1 on 2022-07-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_register_firstname_register_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='firstname',
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, max_length=60, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastname',
            field=models.CharField(blank=True, max_length=60, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='register',
            name='middlename',
            field=models.CharField(blank=True, max_length=60, verbose_name='middlename'),
        ),
    ]
