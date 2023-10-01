from django.contrib.auth.models import User
from django.db import models
from store.models import Game

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.displayname
    

class library(models.Model):
    profile = models.OneToOneField(profile, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return f"{self.profile.displayname}'s Library."
