from django.db import models
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.
class Review(models.Model):
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE, default=None)
    content = models.TextField(blank=True, null=True, default=None, max_length=1000)
    rating = models.BooleanField(default=False)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Developers(models.Model):
    name = models.CharField(max_length=50)
    logo_url = models.URLField()

    def __str__(self):
        return self.name

class Publishers(models.Model):
    name = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Game(models.Model):
    title = models.CharField(max_length=50)
    developer = models.OneToOneField(Developers, on_delete=models.CASCADE, null=True)
    publisher = models.OneToOneField(Publishers, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True, default=None, max_length=1000)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True, default=None)
    price = models.FloatField(blank=False, null=False, default=0.0, max_length=5)
    steamid = models.IntegerField(blank=False, null=False, default=0)
    deal = models.IntegerField(blank=False)

    def get_discounted_price(self):
        if self.deal > 0:
            price_decimal = Decimal(str(self.price))
            discount = (price_decimal * self.deal) / 100
            discounted_price = price_decimal - discount
            return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return self.price

    def __str__(self):
        return self.title

    def getcover(self):
        self.logo.url

class Cart(models.Model):
    user = models.ForeignKey('users.Profile', on_delete=models.CASCADE, default=None)
    games = models.ManyToManyField(Game)

class Game_tags(models.Model):
    game = models.ManyToManyField(Game)
    tags = models.ManyToManyField(Tags)



