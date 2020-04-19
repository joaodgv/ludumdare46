import pygame
import pygame_gui
import time
import sys
from sprites import *
from gamemanager import *
from player import *

def initloop():
	fonttitle = pygame.font.SysFont('Arial', 50)
	Title = fonttitle.render("Alien Daycare Center", 1, (255,255,255))

	description = "Your job is to take care of incoming aliens."
	description2 = "You have to give them Food, water and playing time,"
	description3 = "until their time to leave arrives"
	commands = "left click to walk"
	commands2 = "right click on the baby to deliver it"
	commands3 = "and just go to the baby when he wants to sleep"

	font_desc = pygame.font.SysFont('Arial', 25)
	desc1 = font_desc.render(description, 1, (255,255,255))
	desc2 = font_desc.render(description2, 1, (255,255,255))
	desc6 = font_desc.render(description3, 1, (255,255,255))
	desc3 = font_desc.render(commands, 1, (255,255,255))
	desc4 = font_desc.render(commands2, 1, (255,255,255))
	desc5 = font_desc.render(commands3, 1, (255,255,255))

	manager = pygame_gui.UIManager((800, 600))

	hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 400), (100, 100)),
											 text='Play',
											 manager=manager)

	isrunning = True
	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.USEREVENT:
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
					if event.ui_element == hello_button:
						isrunning = False

			manager.process_events(event)

		window_surface.blit(Title, [200,100])
		window_surface.blit(desc1, [150,200])
		window_surface.blit(desc2, [150,230])
		window_surface.blit(desc6, [150,260])
		window_surface.blit(desc3, [150,290])
		window_surface.blit(desc4, [150,320])
		window_surface.blit(desc5, [150,350])

		manager.draw_ui(window_surface)

		pygame.display.update()


	gameloop()

def gameloop():
	#pygame.mixer.music.load("assets/cry.mp3")
	#pygame.mixer.music.play(2)

	##creating the classes (background, game manager, uimanager, player)
	bg = Background()
	player = Player()
	objects = [Toy(60, 220), Pod(300,300), Pod(450,300), Pod(300,150), Pod(450,150), Water(60, 30), Food(60, 130)]
	gamemanager = GameManager(window_surface)
	uimanager = pygame_gui.UIManager((778, 633))
	end_manager = pygame_gui.UIManager((778, 633))

	## create the ui for the game in motion
	score = gamemanager.score
	label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((678, 0), (100, 25)),
												text='Score: {}'.format(gamemanager.score),
												manager=uimanager)

	playeritem = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (200, 25)),
												text='you are carrying: {}'.format(player.item),
												manager=uimanager)

	## UI for the end screen

	clock = pygame.time.Clock()
	is_running = True

	gamemanager.receive_baby()

	#program loop
	while is_running:
		aliens = gamemanager.get_babies()

		time_delta = clock.tick(60)/1000.0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if(pygame.mouse.get_pressed() == (0,0,1)):
					player.deliver = True
					target = pygame.mouse.get_pos()
					player.target = target
				else:
					target = pygame.mouse.get_pos()
					player.target = target
			

			uimanager.process_events(event)

		## checks if there is movement to be made
		if player.target != (player.sprite.rect.top, player.sprite.rect.left):
			player.move()

		## checks for colisions with the utilities
		for i in objects:
			if player.sprite.rect.colliderect(i.rect):
				if(player.item == "alien" and i.name == "pod" and not i.has_babie):
					player.item = ""
					i.has_babie = True
					i.alien = player.baby
					aliens[player.baby].show = True
					aliens[player.baby].sprite.rect = aliens[player.baby].sprite.rect.move(i.rect.left-aliens[player.baby].sprite.rect.left - 11, i.rect.top-aliens[player.baby].sprite.rect.top + 20)
					aliens[player.baby].show = True
					aliens[player.baby].inpod = True
				elif(player.item != "alien" and i.name != "pod"):
					player.item = i.name
			
			if i.name == "pod" and aliens[i.alien] == None:
				i.has_babie = False

		for a in aliens:
			if player.item != "alien" and a != None:
				if player.sprite.rect.colliderect(a.sprite.rect) and not a.inpod:
					player.item = "alien"
					player.baby = a.tag
					a.show = False
				elif player.sprite.rect.colliderect(a.sprite.rect) and a.inpod and a.get_need() == player.item:
					if player.item == "water":
						a.a_water()			
					if player.item == "food":
						a.a_eat()
					if player.item == "toy":
						a.a_play()
					player.item = ""
				elif player.sprite.rect.colliderect(a.sprite.rect) and a.inpod and a.get_need() == "sleep":
					a.a_sleep()
					player.item = ""
				elif  player.sprite.rect.colliderect(a.sprite.rect) and a.timer <= 0 and player.deliver:
					player.deliver = False
					gamemanager.deliver_baby(a)

		#updates the ui
		label.set_text("score: {}".format(gamemanager.score))
		playeritem.set_text("you are carrying: {}".format(player.item))
		uimanager.update(time_delta)

		if (gamemanager.update(time_delta) == 0):
			window_surface.blit(bg.image, bg.rect)
			end_loop(gamemanager.score)

		#prints on the screen
		window_surface.blit(bg.image, bg.rect)
		
		for i in objects:
			window_surface.blit(i.image, i.rect)

		for a in aliens:
			if a != None:
				if a.show:
					window_surface.blit(a.sprite.image, a.sprite.rect)
					window_surface.blit(a.text, [a.sprite.rect.left+10, a.sprite.rect.top+23])
					window_surface.blit(a.need, [a.sprite.rect.left, a.sprite.rect.top-23])

		window_surface.blit(player.sprite.image, player.sprite.rect)
		uimanager.draw_ui(window_surface)

		pygame.display.update()

def end_loop(score):
	bg = Background()
	is_running = True
	again = False

	manager = pygame_gui.UIManager((800, 600))

	hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 400), (100, 100)), text='Play again', manager=manager)

	goodbye_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 400), (100, 100)), text='Exit', manager=manager)

	label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((250, 250), (200, 25)), text='Tou had a score of {}'.format(score), manager=manager)

	while is_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False

			if event.type == pygame.USEREVENT:
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
					if event.ui_element == hello_button:
						is_running = False
						again = True
					elif event.ui_element == goodbye_button:
						sys.exit()

			manager.process_events(event)

		window_surface.blit(bg.image, bg.rect)

		manager.draw_ui(window_surface)

		pygame.display.update()

	if again:
		gameloop()

#starting the program
pygame.init()

pygame.display.set_caption('Alien daycare center')
window_surface = pygame.display.set_mode((778, 633))

initloop()
