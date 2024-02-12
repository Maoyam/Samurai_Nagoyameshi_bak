# Generated by Django 4.2.6 on 2024-02-12 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_genre_image_delete_genreimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=100)),
                ('price_low', models.CharField(max_length=5)),
                ('price_high', models.CharField(max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='restaurant_images')),
                ('information', models.CharField(max_length=300)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.area')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.genre')),
            ],
        ),
    ]
