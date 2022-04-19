from django.db import models

# Question model
class Question(models.Model):
  topic = models.CharField(max_length=50) # "Animals", "Food", "Travel"
  question = models.CharField(max_length=200)
  used = models.BooleanField(default=False)

class Player(models.Model):
  username = models.CharField(max_length=50)
  userhash = models.CharField(max_length=50)
  question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
  answer = models.TextField()