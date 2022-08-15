# Generated by Django 4.0.5 on 2022-08-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
