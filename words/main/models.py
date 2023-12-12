from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Game(models.Model):
	account = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name = 'Аккаунт', null=True)
	username = models.CharField('Имя игрока 1(загадывает слово)',max_length=16)
	username2 = models.CharField('Имя игрока 2(отгадывает слово)',max_length=16)
	word = models.CharField('Загаданное слово',max_length=25)
	create_date = models.DateTimeField('Дата создания игры',  default=now, editable=True)
	is_game_active = models.BooleanField('Игра не закончена?', default=True)
	game_result = models.BooleanField('Игрок победил?', default=False)
	encrypted_word = models.CharField('Зашифрованное слово',max_length=60)
	number_of_mistakes = models.IntegerField('Количество ошибок', default= 0)
	game_save = models.BooleanField('Игра сохранена?', default=False)
	def __str__(self):
		return str(self.account)

	class Meta:

		verbose_name = "Игра"
		verbose_name_plural = "Игры"
		ordering = ['-create_date']