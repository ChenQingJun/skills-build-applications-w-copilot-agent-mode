from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, to_field="_id")

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="_id")
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="_id")
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    def __str__(self):
        return self.name
