# Generated by Django 5.0 on 2023-12-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_duration_alter_movie_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
