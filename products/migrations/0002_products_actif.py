# Generated by Django 4.0 on 2022-06-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
