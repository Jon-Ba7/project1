
# Create your tests here.

#from selenium import webdriver

#driver = webdriver.Safari

from django.test import TestCase
from .models import Animal
from flask import Flask

class AnimalTestCase(TestCase):
    def setUp(self):
        print("Setup")

    def test_animals_can_speak(self):
        lion = Animal(name="lion", sound="roar", size=12)
        cat = Animal(name="cat", sound="meow", size=1)

        self.assertEqual(lion.speak("roar"), 'The lion says roar')
        self.assertEqual(cat.speak("meow"), 'The cat says meow')
