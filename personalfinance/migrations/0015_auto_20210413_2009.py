# Generated by Django 3.1.1 on 2021-04-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalfinance', '0014_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='euro_amount',
            field=models.IntegerField(default=0),
        ),
    ]