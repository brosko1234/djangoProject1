# Generated by Django 4.1.7 on 2023-03-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0006_alter_basic_image_big_alter_basic_image_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='image_big',
            field=models.FileField(upload_to='trade/'),
        ),
    ]
