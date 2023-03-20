# Generated by Django 4.1.7 on 2023-03-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_basic_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic',
            name='images',
        ),
        migrations.AddField(
            model_name='basic',
            name='image_big',
            field=models.ImageField(default=True, upload_to='trade/'),
        ),
        migrations.AddField(
            model_name='basic',
            name='image_small',
            field=models.ImageField(default=True, upload_to='trade/'),
        ),
    ]