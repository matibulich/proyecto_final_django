# Generated by Django 4.0.4 on 2022-06-26 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('plataforma', models.CharField(max_length=30)),
                ('puntuacion', models.IntegerField()),
                ('comentarios', models.CharField(max_length=300)),
            ],
        ),
    ]
