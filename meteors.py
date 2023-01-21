import pygame
import os
import sys
import random
from Particles import Particle

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


def create_particles(particles, position, vx, vy, count=20):
    particle_count = 20
    if vx > 0:
        x = range(-1, 5)
    elif vx < 0:
        x = range(-5, 1)
    else:
        x = range(-1, 1)
    for _ in range(particle_count):
        Particle(particles, position, random.choice(x), random.choice(x))


img_of_meteors = []
for i in range(1, 3):
    img_of_meteors.append([load_image(f'meteor{i}.png'), i])


class Meteor(pygame.sprite.Sprite):
    def __init__(self, *group, x=None, y=None, vx=None, vy=None):
        super().__init__(*group)
        self.image, self.number_of_img = random.choice(list(map(lambda x: (x[0], x[1]), img_of_meteors)))
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width * 2,
                                                         self.image.get_rect().height * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # ширина изображения для вычисления максимальной горизонтальной скорости
        w = self.image.get_size()[0] / 2
        # стартовая пзиция
        # проверка на наличие входных данных
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
                # придание горизонтальной скорости без вылета за экран
                self.vx = random.randint(-(((self.rect.left - w) / FPS) // ((height // FPS) // self.vy)),
                                    (((width // FPS) - ((self.rect.right - w) // FPS)) // ((height // FPS) // self.vy)))
        # параметры метеорита
        self.damage = 0

    def update(self, reg_shells, reg_meteors, particles, player):
        self.image = load_image(f'meteor{self.number_of_img}.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width * 2,
                                            self.image.get_rect().height * 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.damage >= 5:
            create_particles(particles, (self.rect.x, self.rect.y), self.vx, self.vy)
            self.kill()

        for i in reg_shells:
            # проверка столкновения со снарядами
            if pygame.sprite.collide_mask(self, i):
                self.damage += 1
                if self.damage == 5:
                    player.pl_score += 10
                self.image = load_image(f'meteor{self.number_of_img}blink.png')
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width * 2,
                                                                 self.image.get_rect().height * 2))
                self.mask = pygame.mask.from_surface(self.image)
                i.terminate()

        for i in reg_meteors:
            if self != i and self.rect.y >= 100:
                if pygame.sprite.collide_mask(self, i):
                    create_particles(particles, (self.rect.x, self.rect.y), self.vx, self.vy)
                    self.damage = 5

        if pygame.sprite.collide_mask(self, player):
            for i in reg_meteors:
                if i == self:
                    self.damage = 5
                    create_particles(particles, (self.rect.x, self.rect.y), self.vx, self.vy)
                    self.kill()
                    player.hurt()
        if self.rect.y > 900:
            if not(player.die):
                player.hurt(die=True)
            self.kill()