import pygame
import os
import sys
import random

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


class Shells(pygame.sprite.Sprite):
    def __init__(self, *group, pos, velocity):
        super().__init__(group)
        self.image = image = pygame.Surface([6, 16])
        self.image.fill(pygame.color.Color(255, 255, 100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vy = velocity
        self.damage = 0

    def update(self, reg_meteors):
        self.rect.y -= self.vy

    def terminate(self):
        self.kill()