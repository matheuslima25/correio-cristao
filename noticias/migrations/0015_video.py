# Generated by Django 2.1.5 on 2019-02-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0014_auto_20190204_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
    ]