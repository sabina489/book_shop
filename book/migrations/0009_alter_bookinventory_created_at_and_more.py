# Generated by Django 4.0.1 on 2022-07-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_book_image_url_book_image_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookinventory',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
