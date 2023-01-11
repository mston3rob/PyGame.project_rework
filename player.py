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

class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(group)
        self.pos = (600, 580)
        self.player_image = PLAYER
        self.rect = self.player_image.get_rect()
        self.mask = pygame.mask.from_surface(self.player_image)
        self.shooting = False

    def update_pos_player(self, pos, screen):
        pass

    def update_player_shooting(self, pos, shooting):
        pass