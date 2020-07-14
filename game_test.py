from django.test import TestCase
from model_bakery import baker

class game_test_model(TestCase):
    def setUp(self):
        game = baker.make('Game')
        print(self.game)
