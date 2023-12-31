# Generated by Django 4.2.5 on 2023-11-06 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_game_cover_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo_url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ManyToManyField(to='store.game')),
                ('tags', models.ManyToManyField(to='store.tags')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.developers'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.publishers'),
        ),
    ]
