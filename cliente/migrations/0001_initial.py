# Generated by Django 4.2.10 on 2024-03-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
