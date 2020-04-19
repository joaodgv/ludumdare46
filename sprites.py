#python3
import pygame

## Classes for sprites
class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/Background.png")
		self.rect = self.image.get_rect()
		self.rect.top = 0
		self.rect.left = 0

## alien, food, water, toys, cribs
class AlienBaby(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.name = "alien"
		self.image = pygame.image.load("assets/alien.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(605, 515)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/person.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(250,250)

class Toy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.name = "toy"
		self.image = pygame.image.load("assets/toy.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(x,y)

class Pod(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.name = "pod"
		self.alien = 0
		self.image = pygame.image.load("assets/pod.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(x,y)
		self.has_babie = False

class Food(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.name = "food"
		self.image = pygame.image.load("assets/food.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(x, y)

class Water(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.name = "water"
		self.image = pygame.image.load("assets/bottle.png")
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(x, y)