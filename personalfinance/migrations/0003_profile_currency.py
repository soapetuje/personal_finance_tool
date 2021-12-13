# Generated by Django 3.1.1 on 2021-03-30 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalfinance', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currency',
            field=models.CharField(blank=True, choices=[('AUD', 'Australian dollar'), ('BGN', 'Bulgarian lev'), ('BRL', 'Brazilian real'), ('CAD', 'Canadian dollar'), ('CHF', 'Swiss franc'), ('CNY', 'Chinese yuan renminbi'), ('CZK', 'Czech koruna'), ('DKK', 'Danish krone'), ('GBP', 'Pound sterling'), ('HKD', 'Hong Kong dollar'), ('HRK', 'Croatian kuna'), ('HUF', 'Hungarian forint'), ('IDR', 'Indonesian rupiah'), ('ILS', 'Israeli shekel'), ('INR', 'Indian rupee'), ('ISK', 'Icelandic krona'), ('JPY', 'Japanese yen'), ('KRW', 'South Korean won'), ('MXN', 'Mexican peso'), ('MYR', 'Malasian ringgit'), ('NOK', 'Norwegian krone'), ('NZD', 'New Zealand dollar'), ('PHP', 'Philippine peso'), ('PLN', 'Polish zloty'), ('RON', 'Romanian leu'), ('RUB', 'Russian rouble'), ('SEK', 'Swedish krona'), ('SGD', 'Singapore dollar'), ('THB', 'Thai baht'), ('TRY', 'Turkish lira'), ('USD', 'US dollar'), ('ZAR', 'South African rand')], default='USD', max_length=3),
        ),
    ]