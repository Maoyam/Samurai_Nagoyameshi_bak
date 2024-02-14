# Generated by Django 4.2.6 on 2024-02-14 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commondb', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='review_images/')),
                ('comment', models.TextField()),
                ('restaurant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondb.restaurant')),
            ],
        ),
    ]