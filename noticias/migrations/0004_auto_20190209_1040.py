# Generated by Django 2.1.5 on 2019-02-09 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20190208_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colunista',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='colunista',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='colunista',
            name='telefone',
        ),
    ]
