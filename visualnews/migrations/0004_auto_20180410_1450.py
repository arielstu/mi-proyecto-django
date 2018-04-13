# Generated by Django 2.0.3 on 2018-04-10 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visualnews', '0003_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('publico', models.BooleanField(verbose_name=False)),
                ('fecha_creacion', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('etiquetas', models.CharField(max_length=255)),
                ('puntuacion', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='autor',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualnews.Noticia'),
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
    ]
