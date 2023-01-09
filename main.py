import pygame
import os
import sys
import random
from meteors import Meteor

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
surface = pygame.Surface((width, height))


for _ in range(5):
    Meteor(meteorites)


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
        screen.fill(pygame.Color('Black'))
        meteorites.draw(screen)
        meteorites.update()
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()