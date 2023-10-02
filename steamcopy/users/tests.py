from django.test import TestCase
from django.contrib.auth.models import User
from .models import library, profile
from store.models import Game

# Create your tests here.
class GamesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = profile.objects.create(user=self.user, displayname="testdisplayname")
        self.client.login(username="testuser", password="testpassword")
        self.game1 = Game.objects.create(title="Cyberpynk 2077")
        self.game2 = Game.objects.create(title="Hunt: Showdown")
        library.objects.create(profile=self.profile)

        library.objects.get(profile=self.profile).games.add(self.game1)
        library.objects.get(profile=self.profile).games.add(self.game2)

    def test_number(self):
        response = self.client.get('/user/')
        self.assertContains(response, "Cyberpunk 2077")
        self.assertContains(response, "Hunt: Showdown")

        number = library.objects.filter(profile=self.profile).count()

        self.assertEqual(len(response.context['game'], number))