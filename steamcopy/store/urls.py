from django.contrib import admin
from django.urls import path, include
import store.views as views

urlpatterns = [
    path('', views.homestore, name='homestore'),
    path('game/<int:game_id>', views.game, name='game'),
    path('remove_game/<int:game_id>/', views.remove_game, name='remove_game'),
    path('add_game/<int:game_id>/', views.add_game, name='add_game'),
    path('rate_game/<int:game_id>/', views.rate_game, name='rate_game'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart_view, name='cart'),
    path('remove_from_cart/<int:game_id>/', views.remove_from_cart_view, name="remove_from_cart"),
    path('checkout/', views.buy_cart, name='checkout'),
]
