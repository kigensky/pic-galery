# Generated by Django 3.2.2 on 2021-05-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_image_cloudinary_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]
