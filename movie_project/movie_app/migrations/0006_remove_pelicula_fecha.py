# Generated by Django 4.0.4 on 2022-07-16 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_pelicula_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='fecha',
        ),
    ]