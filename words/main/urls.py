from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('sing_in/', views.sing_in, name = 'sing_in'),
	path('games_history/', views.games_history, name = 'games_history'),
	path('active_games/', views.active_games, name = 'active_games'),
	path('register/', views.register, name='register'),
	path('logout/', views.logout_view, name='logout'),
	path('save_game/', views.save_game, name='save_game'),
	path('create_game/', views.create_game, name='create_game'),
]