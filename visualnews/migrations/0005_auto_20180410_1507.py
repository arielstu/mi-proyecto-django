# Generated by Django 2.0.3 on 2018-04-10 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visualnews', '0004_auto_20180410_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actualizacion', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('voto', models.BooleanField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='puntuacion',
            new_name='puntos',
        ),
        migrations.AddField(
            model_name='puntuacion',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualnews.Noticia'),
        ),
    ]
