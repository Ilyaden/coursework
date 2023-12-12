# Generated by Django 4.0.4 on 2023-12-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_game_encrypted_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='number_of_mistakes',
            field=models.IntegerField(default=0, verbose_name='Количество ошибок'),
        ),
        migrations.AlterField(
            model_name='game',
            name='encrypted_word',
            field=models.CharField(max_length=60, verbose_name='Зашифрованное слово'),
        ),
    ]