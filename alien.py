#python3 file
from random import randrange
from sprites import AlienBaby

class Alien():
    def __init__(self, tag):
      self.tag = tag
      self.life = 100
      self.sprite = AlienBaby()
      self.water = randrange(50, 100)
      self.food = randrange(50, 100)
      self.sleep = randrange(50, 100)
      self.play = randrange(50, 100)
    
    def get_need(self):
      if(self.food < 50):
        return "food"
      elif(self.water < 50):
        return "water"
      elif(self.sleep < 50):
        return "sleep"
      elif(self.play < 50):
        return "play"
      else:
        return None

    def update_life(self):
      if(self.food < 45):
        self.life -= 4
      elif(self.water < 45):
        self.life -= 4
      elif(self.sleep < 45):
        self.life -= 4
      elif(self.play < 45):
        self.life -= 4
    
    def eat(self):
      self.food += 10

    def water(self):
      self.water += 15

    def sleep(self):
      self.food += 30

    def play(self):
      self.food += 5

    def update(self):
      self.food -= 1
      self.water -= 1
      self.sleep -= 1
      self.play -= 1