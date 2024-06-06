from django.urls import path, include
from .views import Home, GamesView, SpielerListView, SpielerCreateView, SpielerUpdateView, Uebersicht, Help
from django.contrib.auth import views
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('Games/', views.GamesView, name='gamesView'),
    path('Spieler/', SpielerListView.as_view()),
    path('Spieler/create/', SpielerCreateView.as_view(), name='createNew'),
    path('Spieler/update/<pk>', SpielerUpdateView.as_view(), name='update'),
    path('Overview/', views.Uebersicht, name='overview'),
    path('Help/', views.Help, name='help'),

]