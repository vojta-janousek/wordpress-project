# Generated by Django 2.1 on 2019-03-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptvc_app', '0008_remove_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='me@plastictree.com', max_length=100),
        ),
    ]
