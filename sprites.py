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
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.top = 605
        self.rect.left = 516

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/person.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0