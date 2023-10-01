from django.db import models

# Create your models here.
class Review(models.Model):
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE, default=None)
    content = models.TextField(blank=True, null=True, default=None, max_length=1000)
    rating = models.BooleanField(default=False)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True, default=None, max_length=1000)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True, default=None)

    def getcover(self):
        self.logo.url