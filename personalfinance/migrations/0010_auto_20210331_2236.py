# Generated by Django 3.1.1 on 2021-04-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalfinance', '0009_price_eur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='aud',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='bgn',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='brl',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='cad',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='chf',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='cny',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='czk',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='dkk',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='eur',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='gbp',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='hkd',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='hrk',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='huf',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='idr',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='ils',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='inr',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='isk',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='jpy',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='krw',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='mxn',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='myr',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='nok',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='nzd',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='php',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='pln',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='ron',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='rub',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='sek',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='sgd',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='thb',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='tury',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='usd',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='zar',
            field=models.DecimalField(decimal_places=10, max_digits=30),
        ),
    ]
