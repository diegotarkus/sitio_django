# Generated by Django 4.2.1 on 2023-06-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_artista_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concierto',
            name='venta',
            field=models.CharField(max_length=250, null=True, verbose_name='Link de venta'),
        ),
    ]
