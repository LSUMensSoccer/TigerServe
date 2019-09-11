from django.shortcuts import render


# Create your views here.
from tigerweb.models import Officer, Player, Event


def index(request):
    return render(request, 'tigerweb/index.html')


def about(request):
    return render(request, 'tigerweb/about.html', {'officers': Officer.objects.all().order_by('order')})


def team(request):
    return render(request, 'tigerweb/team.html', {'players': Player.objects.all().order_by('name')})


def contact(request):
    return render(request, 'tigerweb/contact.html')

def schedule(request):
    return render(request, 'tigerweb/schedule.html', {'events': Event.objects.all().order_by('date')})