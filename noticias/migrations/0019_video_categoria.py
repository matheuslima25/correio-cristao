# Generated by Django 2.1.5 on 2019-02-06 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0018_auto_20190205_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.Categoria'),
        ),
    ]