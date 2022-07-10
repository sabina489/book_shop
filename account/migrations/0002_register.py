# Generated by Django 4.0.1 on 2022-07-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(blank=True, help_text='Use\'[algo]$[salt]$[hexdigest]\' or use the                 < a href="password/">change password form</a>.', max_length=128, null=True, verbose_name='password')),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registers',
            },
        ),
    ]