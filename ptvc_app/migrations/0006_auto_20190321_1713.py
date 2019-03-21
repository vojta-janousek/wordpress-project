# Generated by Django 2.1 on 2019-03-21 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ptvc_app', '0005_day_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default="me@plastictree.com", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.PositiveIntegerField(default=123456789),
            preserve_default=False,
        ),
    ]