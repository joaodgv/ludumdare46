import pygame
import pygame_gui
from sprites import *
from gamemanager import *
from player import *

pygame.init()

pygame.display.set_caption('Alien daycare center')
window_surface = pygame.display.set_mode((778, 633))

bg = Background()
player = Player()
gamemanager = GameManager(window_surface)
uimanager = pygame_gui.UIManager((778, 633))

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            target = pygame.mouse.get_pos()
            player.target = target
        
        uimanager.process_events(event)

    if player.target != (player.sprite.rect.top, player.sprite.rect.left):
        player.move()

    uimanager.update(time_delta)

    window_surface.blit(bg.image, bg.rect)
    window_surface.blit(player.sprite.image, player.sprite.rect)
    uimanager.draw_ui(window_surface)

    pygame.display.update()