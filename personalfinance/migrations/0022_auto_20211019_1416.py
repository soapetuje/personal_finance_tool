# Generated by Django 3.1.1 on 2021-10-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalfinance', '0021_auto_20211019_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('NH', 'No High School'), ('HS', 'High School Diploma or GED'), ('AS', "Associate's Degree"), ('BS', "Bachelor's Degree"), ('MS', "Master's Degree"), ('DC', 'Doctorate Degree'), ('PD', 'Professional Degree'), ('OT', 'Other')], default='OT', max_length=2),
        ),
    ]
