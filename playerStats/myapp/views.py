from django.shortcuts import render, HttpResponse
from .models import playerModel


# Create your views here.
def home(request):
	return HttpResponse("Welcome to StatShow") 

def playerList(request): #just outputs all of the data from the db
	posts=playerModel.objects.all()
	return render(request, "playerList.html",{"posts": posts})


def searchPlayer(request):
    player_name = request.GET.get('player', '')

    if player_name:
        posts = playerModel.objects.raw("SELECT * FROM playerstats WHERE player LIKE %s", [player_name])
    else:
        posts = []  

    return render(request, "search.html", {"posts": posts, "player_name": player_name})

def searchbyTeam(request):
    team_name = request.GET.get('squad', '')

    if team_name:
        posts = playerModel.objects.raw("SELECT * FROM playerstats WHERE squad=%s", [team_name])
    else:
        posts = []  

    return render(request, "team.html", {"posts": posts, "team_name": team_name})
