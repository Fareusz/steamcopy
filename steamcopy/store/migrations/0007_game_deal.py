# Generated by Django 4.2.5 on 2023-11-22 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_game_steamid'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='deal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
