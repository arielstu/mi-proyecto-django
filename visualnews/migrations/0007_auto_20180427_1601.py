# Generated by Django 2.0.3 on 2018-04-27 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualnews', '0006_auto_20180422_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
