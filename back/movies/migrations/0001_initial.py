# Generated by Django 4.2.8 on 2024-05-21 07:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.TextField(blank=True, null=True)),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('popularity', models.FloatField()),
                ('backdrop_path', models.TextField(blank=True, null=True)),
                ('adult', models.BooleanField()),
                ('original_language', models.TextField()),
                ('favorite_users', models.ManyToManyField(related_name='favorite_movies', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(to='movies.genre')),
                ('hate_users', models.ManyToManyField(related_name='hate_movies', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
