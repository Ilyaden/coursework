from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='sing_in')
def home(request):
	account = request.user
	games = Game.objects.filter(Q(account = account) & Q(is_game_active = True))
	save_games = Game.objects.filter(Q(account = account) & Q(is_game_active = True) & Q(game_save=False))
	if (games and (len(save_games) == 1)):

		
		encrypted_word = save_games[0].encrypted_word
		new_encrypted_word = encrypted_word.replace("_", "_ ")
		word = save_games[0].word
		number_of_mistakes = save_games[0].number_of_mistakes
		if request.method == 'POST':
			form = GameForm(request.POST)
			if form.is_valid():
				letter = form.cleaned_data['letter']
				if letter in word:
					indices = []
					for index, char in enumerate(word):
						if char == letter:
							indices.append(index)		

					encrypted_word_list = list(encrypted_word)
					word_list = list(word)
					
					for x in indices:
						encrypted_word_list[x] = word_list[x]

					
					encrypted_word = "".join(encrypted_word_list)
					new_encrypted_word = encrypted_word.replace("_", "_ ")

					save_games[0].encrypted_word = encrypted_word 

					save_games[0].save()

					if (encrypted_word == word):
						save_games[0].is_game_active = False
						save_games[0].game_result = True
						save_games[0].save()

					else:
						return redirect('home')

				else:
					number_of_mistakes+=1
					save_games[0].number_of_mistakes = number_of_mistakes
					save_games[0].save()

					if number_of_mistakes == 7:
						save_games[0].is_game_active = False
						save_games[0].game_result = False
						save_games[0].save()

					else:
						return redirect('home')
		
		
		else:
			form = GameForm()
		return render(request, 'main/index.html',{'account':account, 'games':save_games[0], 'form':form, 'encrypted_word':new_encrypted_word, 'number_of_mistakes':number_of_mistakes})

	elif (request.method == 'GET' and request.GET.get('game_id')):
		
		game_id = request.GET.get('game_id')
		games = Game.objects.filter(Q(account = account) & Q(is_game_active = True) & Q(pk = game_id))
		encrypted_word = games[0].encrypted_word
		number_of_mistakes = games[0].number_of_mistakes
		game = games[0]
		game.game_save = False
		game.save()		
		form = GameForm(request.POST)
		new_encrypted_word = encrypted_word.replace("_", "_ ")
		return redirect('home')


	elif (len(games)>1):
		games = False
	
		return render(request, 'main/index.html',{'games':games })
	else:
		if request.method == 'POST':
			form = StartGameForm(request.POST)

			if form.is_valid():
				username = form.cleaned_data['username']
				username2 = form.cleaned_data['username2']
				word = form.cleaned_data['word']
				word_length = len(word)
				encrypted_word = '_' * word_length
				game = Game(account=request.user, username=username, username2=username2, word=word, encrypted_word = encrypted_word)
				game.save()
				return redirect('home')

		else:
			form = StartGameForm()

		return render(request, 'main/index.html',{'form': form,'account':account, 'games':games})

def register(request):
	error_message = ""
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password1'])
			login(request, user)
			return redirect('home')

		else:
			if (form.errors.get('username')):
				error_message = form.errors.get('username')

			elif (form.errors.get('password1')):
				error_message = form.errors.get('password1')

			else:
				error_message = form.errors.get('password2')

	else:
		form = RegisterForm()

	return render(request, 'main/register.html', {'form': form, 'error_message': error_message})


def sing_in(request):
	error_message = ""
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home')

				else:
					return HttpResponse('Disabled account')

			else:
				error_message = 'Неверный логин или пароль'
	else:
		form = LoginForm()

	return render(request, 'main/login.html', {'form': form, 'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('home')

def games_history(request):
	account = request.user
	games = Game.objects.filter(Q(account = account) & Q(is_game_active = False))
	return render(request, 'main/games_history.html', {'games':games, 'account':account})

def active_games(request):
	account = request.user
	save_games = Game.objects.filter(Q(account = account) & Q(is_game_active = True) & Q(game_save=False))
	games = Game.objects.filter(Q(account = account) & Q(is_game_active = True) )
	if (len(save_games) == 0):
		save_games = True
	else:
		save_games = False 
	return render(request, 'main/active_games.html', {'games':games, 'account':account, 'save_games':save_games})


def save_game(request):

	game_id = request.GET.get('game_id')

	account = request.user
	games = Game.objects.filter(pk=game_id)
	game = games[0]
	game.game_save = True
	game.save()	
	return redirect('home')

def create_game(request):
	if request.method == 'POST':
		form = StartGameForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			username2 = form.cleaned_data['username2']
			word = form.cleaned_data['word']
			word_length = len(word)
			encrypted_word = '_' * word_length
			game = Game(account=request.user, username=username, username2=username2, word=word, encrypted_word = encrypted_word)
			game.save()
			return redirect('home')
	else:
		form = StartGameForm()

	return render(request, 'main/create_game.html', {'form':form})






