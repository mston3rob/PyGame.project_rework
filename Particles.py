import pygame
import random
import os
import sys

pygame.init()
size = width, height = 1200, 840
# ширина экрана должна быть кратна фреймрету (FPS)
screen = pygame.display.set_mode(size)
# инициализация спрайтов метеоритов
meteorites = pygame.sprite.Group()
# список из изображений метеоритов (длинна=9)
shells = pygame.sprite.Group()
FPS = 60

screen_rect = (0, 0, width, height)


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


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("meteor1.png")]
    for scale in (5, 5, 10):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, group, pos, dx, dy):
        super().__init__(group)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.3

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()