# Generated by Django 2.0.13 on 2019-04-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_pick', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='movie_name',
            new_name='movie',
        ),
    ]
