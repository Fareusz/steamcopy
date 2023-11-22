from django.contrib import admin
from django.urls import path, include
import homepage.views as views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('user/', include('users.urls'), name='users'),
    path('store/', include('store.urls'), name='store'),
]
