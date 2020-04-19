import pygame
import pygame_gui
from sprites import *
from gamemanager import *
from player import *

#starting the program
pygame.init()

pygame.display.set_caption('Alien daycare center')
window_surface = pygame.display.set_mode((778, 633))

##creating the classes (background, game manager, uimanager, player)
bg = Background()
player = Player()
objects = [Toy()]
gamemanager = GameManager(window_surface)
uimanager = pygame_gui.UIManager((778, 633))

## create the ui for the game in motion
score = gamemanager.score
label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((678, 0), (100, 25)),
											 text='Score: {}'.format(gamemanager.score),
											 manager=uimanager)
clock = pygame.time.Clock()
is_running = True

#program loop
while is_running:
	aliens = gamemanager.get_babies()

	time_delta = clock.tick(60)/1000.0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			#later on we will divide the buttons into left and right
			target = pygame.mouse.get_pos()
			player.target = target
		

		uimanager.process_events(event)

	## checks if there is movement to be made
	if player.target != (player.sprite.rect.top, player.sprite.rect.left):
		player.move()

	## checks for colisions with the utilities
	for i in objects:
		if player.sprite.rect.colliderect(i.rect):
			if(player.item == ""):
				player.item = i.name


	#updates the ui
	label.set_text("score: {}".format(gamemanager.score))
	uimanager.update(time_delta)

	#prints on the screen
	window_surface.blit(bg.image, bg.rect)
	
	for i in objects:
		window_surface.blit(i.image, i.rect)

	window_surface.blit(player.sprite.image, player.sprite.rect)
	uimanager.draw_ui(window_surface)

	pygame.display.update()