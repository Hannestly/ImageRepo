# Generated by Django 3.1.4 on 2020-12-29 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_image_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='temp_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
