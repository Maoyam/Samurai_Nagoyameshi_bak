# Generated by Django 4.2.6 on 2024-02-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondb', '0018_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
    ]