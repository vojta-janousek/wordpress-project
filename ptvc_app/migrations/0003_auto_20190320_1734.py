# Generated by Django 2.1 on 2019-03-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptvc_app', '0002_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptvc_app.Subject'),
        ),
    ]
