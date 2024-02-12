# Generated by Django 4.2.6 on 2024-02-12 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='genre_images')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_alphabet', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=100)),
                ('price_low', models.CharField(max_length=5)),
                ('price_high', models.CharField(max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='restaurant_images')),
                ('information', models.CharField(max_length=300)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondb.area')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondb.genre')),
            ],
        ),
    ]
