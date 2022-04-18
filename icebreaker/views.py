from django.shortcuts import render
from django.http import HttpResponse

def server(request):
    return render(request, 'icebreaker/server.html')

def player(request):
    return render(request, 'icebreaker/player.html')
  
def index(request):
    return render(request, 'icebreaker/index.html')