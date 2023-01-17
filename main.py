import pygame
import os
import sys
import random
from meteors import Meteor
from shells import Shells
from player import Player
from menu import Menu

# инициалитзация pygame для работы со спрайтами и загрузкой изображения
pygame.init()
size = width, height = 1200, 840
# ширина экрана должна быть кратна фреймрету (FPS)
screen = pygame.display.set_mode(size)
# инициализация спрайтов метеоритов
meteorites = pygame.sprite.Group()
particles = pygame.sprite.Group()
shells = pygame.sprite.Group()
FPS = 60
fire_rate = 200

SHOT_TIMING = pygame.USEREVENT + 1
# создание списков для храения объектов 2х классов, для проверки пересечения по маске
reg_meteors = []
reg_shells = []

for i in range(5):
    reg_meteors.append([Meteor(meteorites, id=i), 0])

#reg_meteors.append([Meteor(meteorites,vy=1, x=0, vx=1, id=4), 0])
#reg_meteors.append([Meteor(meteorites,vy=1, x=500, vx=-1, id=5), 0])

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)
    running = True
    shooting = False
    stop = False
    clock = pygame.time.Clock()
    cursor_pos = None
    player = Player()
    menu = Menu(width, height)
    pygame.time.set_timer(SHOT_TIMING, fire_rate)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop = True
            if event.type == pygame.QUIT:
                running = False
            if not stop:
                if event.type == pygame.MOUSEMOTION:
                    cursor_pos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # создание снаряда (тест при нажатии)
                    shooting = True
                if event.type == pygame.MOUSEBUTTONUP:
                    shooting = False
                if event.type == SHOT_TIMING and shooting:
                    reg_shells.append([Shells(shells, pos=(player.get_pos()), velocity=10), 0])
        if stop:
            menu.go_menu(screen)
            menu.menu_ok, stop= True, False
        else:
            screen.fill(pygame.Color('Black'))
            if pygame.mouse.get_focused() and cursor_pos:
                player.update(cursor_pos[0])
            player.draw(screen)
            shells.draw(screen)
            shells.update(reg_meteors)
            meteorites.draw(screen)
            meteorites.update(reg_shells, reg_meteors, particles, player)
            particles.draw(screen)
            particles.update()
            player.hearts()
            clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()