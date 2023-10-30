from django.contrib import admin
from .models import Game, Tags, Game_tags

admin.site.register(Game)
admin.site.register(Tags)
admin.site.register(Game_tags)