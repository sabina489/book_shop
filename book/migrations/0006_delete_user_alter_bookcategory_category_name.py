# Generated by Django 4.0.1 on 2022-07-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_rename_user_firstname_user_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
    ]
