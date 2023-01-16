import pygame
import os
import sys
import random
from meteors import Meteor
from shells import Shells

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

# создание списков для храения объектов 2х классов, для проверки пересечения по маске
reg_meteors = []
reg_shells = []


reg_meteors.append([Meteor(meteorites,vy=1, x=0, vx=1, id=0), 0])
reg_meteors.append([Meteor(meteorites,vy=1, x=500, vx=-1, id=1), 0])

print(reg_meteors)
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # создание снаряда (тест при нажатии)
                reg_shells.append([Shells(shells, pos=event.pos, velocity=10), 0])

        screen.fill(pygame.Color('Black'))
        shells.draw(screen)
        shells.update(reg_meteors)
        meteorites.draw(screen)
        meteorites.update(reg_shells, reg_meteors, particles)
        particles.draw(screen)
        particles.update()
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()