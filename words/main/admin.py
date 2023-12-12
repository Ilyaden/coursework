from django.contrib import admin
from .models import *
# Register your models here.
class GameAdmin(admin.ModelAdmin):
    search_fields = ('name',)
   

admin.site.register(Game, GameAdmin)