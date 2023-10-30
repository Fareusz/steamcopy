# Generated by Django 4.2.5 on 2023-10-30 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_developers_publishers_tags_game_cover_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.developers'),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.publishers'),
        ),
    ]
