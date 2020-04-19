#python3 file
from random import randrange
from sprites import AlienBaby
import pygame

class Alien():
	def __init__(self, tag):
		self.tag = tag
		self.life = 400
		self.sprite = AlienBaby()
		self.font = pygame.font.SysFont('Arial', 18)
		self.water = randrange(50, 100)
		self.food = randrange(50, 100)
		self.sleep = randrange(50, 100)
		self.play = randrange(50, 100)
		self.show = True	
		self.inpod = False
		self.text = self.font.render("LIFE: {}".format(round(self.life/4), 0), 1, (0,0,0))
		self.need = self.font.render("", 1, (0,0,0))
		self.timer = randrange(30, 60)

	def get_need(self):
		if self.timer <= 0:
			self.need = self.font.render("TIME!!!", 1, (0,0,0))
		else:
			if(self.food < 50):
				self.need = self.font.render("FOOD", 1, (0,0,0))
				return "food"
			elif(self.water < 50):
				self.need = self.font.render("WATER", 1, (0,0,0))
				return "water"
			elif(self.sleep < 50):
				self.need = self.font.render("SLEEP", 1, (0,0,0))
				return "sleep"
			elif(self.play < 50):
				self.need = self.font.render("PLAY", 1, (0,0,0))
				return "toy"
			else:
				self.need = self.font.render("", 1, (0,0,0))

	def a_eat(self):
		self.food += 20

	def a_water(self):
		self.water += 35

	def a_sleep(self):
		self.sleep += 30

	def a_play(self):
		self.play += 15

	def update(self, time):
		self.food -= time*1.3
		self.water -= time*1.3
		self.sleep -= time*1.3
		self.play -= time*1.3

		self.get_need()

		self.life = self.food + self.water + self.sleep + self.play
		self.text = self.font.render("LIFE: {}".format(round(self.life/4), 0), 1, (255,0,0))
		self.timer = self.timer - time