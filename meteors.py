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
surface = pygame.Surface((width, height))


# функция загрузки изоражения из папки data
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


img_of_meteors = []
for i in range(1, 10):
        img_of_meteors.append([load_image(f'meteor{i}.png'), i])


class Meteor(pygame.sprite.Sprite):
    def __init__(self, *group, x=None, y=None, vx=None, vy=None):
        super().__init__(*group)
        self.image, self.number_of_img = random.choice(list(map(lambda x: (x[0], x[1]), img_of_meteors)))
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width * 2,
                                                         self.image.get_rect().height * 2))
        self.rect = self.image.get_rect()
        # ширина изображения для вычисления максимальной горизонтальной скорости
        w = self.image.get_size()[0] / 2
        # стартовая пзиция
        if x != None:
            self.rect.x = x
        else:
            self.rect.x = random.randint(0, width - self.rect.width)
        if y != None:
            self.rect.y = y
        else:
            self.rect.y = 0
        # скорость
        if vy != None:
            self.vy = vy
        else:
            self.vy = random.randint(3, 5)
        # перемещение методом rect.move() работает не покадрово а за каждый тик (1000 раз в секунду),
        # поэтому указываем скорось в пикселях, деленных на фреймрейт
        if vx != None:
            self.vx = vx
        else:
            if self.vy:
                self.vx = random.randint(-(((self.rect.left - w) / FPS) // ((height // FPS) // self.vy)),
                                    (((width // FPS) - ((self.rect.right - w) // FPS)) // ((height // FPS) // self.vy)))
        # параметры метеорита
        self.damage = 0

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy