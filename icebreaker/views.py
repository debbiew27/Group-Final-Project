from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from icebreaker.models import *
from django.views.decorators.csrf import csrf_exempt
import json
import random

def server(request):
  global populate
  # clear entire database first with questions?
  # then populate here
  populate_database()
  return render(request, 'icebreaker/server.html')

def player(request):
  return render(request, 'icebreaker/player.html')
  
def index(request):
  return render(request, 'icebreaker/index.html')

def randomQuestion(dataTopic):
  qSet = Question.objects.filter(topic = dataTopic, used = False)
  r = random.randrange(0, len(qSet)-1)
  it = qSet.iterator()
  for i in range(r):
    it.next()
  return it

@csrf_exempt
def add_player(request, username="DefaultUsername"):
  if request.POST:
    # create new player object in the database
    print("Received POST request with data:")
    data = json.loads(request.body.decode('UTF-8'))
    print(data)
    if(not Player.objects.filter(username=data["username"]).exists()):
      # New player to add
      print("within username check. if nothing else prints, check if questions were initialized")
      if(Question.objects.filter(topic = data["topic"]).exists()):
        # TODO maybe make random later
        print('adding question of type: ', data["topic"])
        #query = Question.objects.filter(topic = data["topic"], used=False).last() 
        query = randomQuestion(data["topic"])
        print("question: ", query.question)
        query.used = True
        query.save()
        new_player = Player(username=data["username"], userhash=data["userhash"], question=query, answer="") 
        new_player.save()
    else:
      print("POPULATING ANSWER FOR ", data["username"])
      # fetch player object and fill in their answer to the question
      if(Player.objects.filter(username=data["username"]).exists()):
        query = Player.objects.filter(username=data["username"]).last()
        query.answer = data["answer"]
        query.save()
    return HttpResponse(True)
  elif request.method == "GET":
    # GET request
    print("request: ", request)
    # fetch all of the players in one go, to be used when running the game
    all_players = []
    try:
      for player in Player.objects.all():
        new_dict = {"username": player.username,
                   "userhash": player.userhash,
                   "question": player.question.question,
                   "answer": player.answer}
        
        all_players.append(new_dict)
    except:
      print("ERROR! NO PLAYERS IN THE DATABASE")
      pass
    return JsonResponse({
      "players": all_players
    })
  else :
    print("making delete call")
    try:
      Player.objects.all().delete()
      Question.objects.all().delete()
      populate_database()
    except:
      print("ERROR! COULDN'T DELETE ALL PLAYERS IN THE DATABASE")
      pass
    return HttpResponse(True)

def populate_database():
  # Food 
  print("Populating Question")
  if(not Question.objects.filter(topic = "Food").exists()):
    Question(topic="Food",question="If you could eat anything in the world right now, what would it be?",used=False).save()
    Question(topic="Food",question="What’s your favorite cuisine/restaurant?",used=False).save()
    Question(topic="Food",question="What would your last meal be?",used=False).save()
    # Question(topic="Food",question="Least favorite food?",used=False).save()
    Question(topic="Food",question="Where is your ideal date night eating spot?",used=False).save()
    Question(topic="Food",question="What meal reminds you most of home?",used=False).save()
    Question(topic="Food",question="Which is better? A picnic in the park or a meal in a restaurant? Why?",used=False).save()
    Question(topic="Food",question="What is the most USELESS tool in the kitchen?",used=False).save()
    
    # Animals
    Question(topic="Animals",question="What is your favorite animal?",used=False).save()
    Question(topic="Animals",question="If you could have any animal in the world as a pet, what would it be?",used=False).save()
    Question(topic="Animals",question="How many pets do you have? What are they?",used=False).save()
    Question(topic="Animals",question="What animal scares you the most? Why?",used=False).save()
    
    # Travel
    Question(topic="Travel",question="Where is your dream vacation?",used=False).save()
    Question(topic="Travel",question="How many countries have you travelled to?",used=False).save()
    Question(topic="Travel",question="How many road trips have you done? To where?",used=False).save()
    Question(topic="Travel",question="Favorite vacation memory?",used=False).save()
    Question(topic="Travel",question="If you're headed out of state, what's your preferred method of travel?",used=False).save()
    Question(topic="Travel",question="Any entertaining airport TSA stories?",used=False).save()
    Question(topic="Travel",question="What are your opinions on American public transit?",used=False).save()