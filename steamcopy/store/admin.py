from django.contrib import admin
from .models import Game, Tags, Game_tags, Developers, Publishers, Cart

admin.site.register(Game)
admin.site.register(Tags)
admin.site.register(Game_tags)
admin.site.register(Developers)
admin.site.register(Publishers)
admin.site.register(Cart)