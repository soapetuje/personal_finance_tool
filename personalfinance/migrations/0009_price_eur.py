# Generated by Django 3.1.1 on 2021-04-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalfinance', '0008_auto_20210331_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='eur',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=30),
        ),
    ]