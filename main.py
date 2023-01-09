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
# список из изображений метеоритов (длинна=9)
shells = pygame.sprite.Group()
FPS = 60

reg_meteors = []
reg_shells = []

for i in range(1):
    reg_meteors.append([Meteor(meteorites,vy=1, id=i), 0])


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 840
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                reg_shells.append([Shells(shells, pos=event.pos, velocity=10), 0])

        screen.fill(pygame.Color('Black'))
        shells.draw(screen)
        shells.update(reg_meteors)
        meteorites.draw(screen)
        meteorites.update(reg_shells)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()