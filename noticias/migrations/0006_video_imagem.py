# Generated by Django 2.1.5 on 2019-02-24 02:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20190210_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='imagem',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagem'),
        ),
    ]
