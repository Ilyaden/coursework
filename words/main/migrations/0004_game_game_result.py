# Generated by Django 4.0.4 on 2023-12-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_game_is_game_active_alter_game_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_result',
            field=models.BooleanField(default=False, verbose_name='Игрок победил?'),
        ),
    ]
