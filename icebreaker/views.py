from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from icebreaker.models import *
from django.views.decorators.csrf import csrf_exempt
import json

populate = False
def server(request):
  global populate
  # clear entire database first with questions?
  # then populate here
  if(not populate):
    populate_database()
    populate = True
  return render(request, 'icebreaker/server.html')

def player(request):
  return render(request, 'icebreaker/player.html')
  
def index(request):
  return render(request, 'icebreaker/index.html')

@csrf_exempt
def add_player(request, username="DefaultUsername"):
  if request.POST:
    # create new player object in the database
    print("Received POST request with data:")
    data = json.loads(request.body.decode('UTF-8'))
    print(data)
    if(not Player.objects.filter(username=data["username"]).exists()):
      # New player to add
      if(Question.objects.filter(topic = data["topic"]).exists()):
        # TODO maybe make random later
        print('adding question of type: ', data["topic"])
        query = Question.objects.filter(topic = data["topic"], used=False).last() 
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
  else:
    # GET request
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

# icebreaker/animalQuestion
# Question -> JSON (Question: Do you like cats)
def question(request):
  if request.GET:
    data = json.loads(request.body.decode('UTF-8'))
    requested_topic = data["topic"]

    if(Question.objects.filter(topic = requested_topic).exists()):
      # TODO maybe make random later
      query = Question.objects.filter(topic = requested_topic, used=False).last() 

      data = query.question
      query.used = True
      query.save()
      
      # how to define endpoint?


def populate_database():
  # Food 
  print("Populating Question")
  Question(topic="Food",question="If you could eat anything in the world right now what would it be?",used=False).save()
  Question(topic="Food",question="What’s your favorite cuisine/restaurant?",used=False).save()
  Question(topic="Food",question="What would your last meal be?",used=False).save()
  Question(topic="Food",question="Least favorite food?",used=False).save()
  Question(topic="Food",question="You’re going on a date. What do you take your date to eat?",used=False).save()
  Question(topic="Food",question="What meal reminds you most of home?",used=False).save()
  Question(topic="Food",question="Does pineapple belong on pizza? If so, explain why?",used=False).save()
  
  # Animals
  Question(topic="Animals",question="What is your favorite animal?",used=False).save()
  Question(topic="Animals",question="What animal scares you the most?",used=False).save()
  Question(topic="Animals",question="If you could have any animal in the world as a pet, what would it be?",used=False).save()
  Question(topic="Animals",question="How many pets do you have?",used=False).save()
  Question(topic="Animals",question="Do you have a pet? What's their name?",used=False).save()
  
  # Travel
  Question(topic="Travel",question="Where is your dream vacation?",used=False).save()
  Question(topic="Travel",question="Favorite vacation memory?",used=False).save()
  Question(topic="Travel",question="How many countries have you travelled to",used=False).save()
  Question(topic="Travel",question="How many road trips have you done? To Where?",used=False).save()