# Generated by Django 4.2.10 on 2024-03-09 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
