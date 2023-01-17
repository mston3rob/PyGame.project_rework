import pygame
import os
import sys


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

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # конвертирование изображения для обрезки фона
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

PLAYER = load_image('player.png', -1)
HEART_POINT = load_image('heart_point.png', -1)

class Player:
    def __init__(self):
        self.player_image = PLAYER
        self.hp_image = HEART_POINT
        self.rect = self.player_image.get_rect()
        self.rect.x, self.rect.y = 580, 700
        self.mask = pygame.mask.from_surface(self.player_image)
        self.shooting = False
        self.what_gun = False
        self.player_hp = 3

    def update(self, cursor_pos_x=580):
        self.rect.x = cursor_pos_x

    def get_pos(self):
        x_from_gun = self.rect.x - 20 if self.what_gun else self.rect.x + 20
        self.what_gun = False if self.what_gun else True
        return (x_from_gun, self.rect.y)

    def draw(self, screen):
        return screen.blit(PLAYER, (self.rect.x - 44, self.rect.y))

    def hurt(self):
        self.player_hp -= 1
        if self.player_hp == 0:
            print('You Lose')

    def hearts(self):
        for i in range(self.player_hp):
            screen.blit(self.hp_image, (1000 + i * 36, 40))