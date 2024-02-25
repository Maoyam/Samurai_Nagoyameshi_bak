# Generated by Django 4.2.6 on 2024-02-25 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondb', '0016_booking_booking_time_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='numbers_of_ppl',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(8)], verbose_name='予約人数'),
        ),
    ]
