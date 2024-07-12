from django.urls import path
from . import views

urlpatterns=[
path("", views.home, name='home'),
path("playerList/",views.playerList, name='players'),
path("search/", views.searchPlayer, name='searchPlayer'),
path("team/", views.searchbyTeam, name='searchbyTeam')
]