import pygame
import os
import sys
from Animation import AnimatedSprite
from win_or_lose import Player_End

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
    def __init__(self, TRAINING):
        self.player_image = PLAYER
        self.hp_image = HEART_POINT
        self.rect = self.player_image.get_rect()
        self.rect.x, self.rect.y = 580, 700
        self.mask = pygame.mask.from_surface(self.player_image)
        self.shooting = False
        self.what_gun = False
        self.player_hp = 3
        self.pl_score = 0
        self.die = False
        self.training = TRAINING
        self.player_end = Player_End()

    def update(self, cursor_pos_x=580):
        self.rect.x = cursor_pos_x

    def get_pos(self):
        x_from_gun = self.rect.x - 20 if self.what_gun else self.rect.x + 20
        self.what_gun = False if self.what_gun else True
        return (x_from_gun, self.rect.y)

    def draw(self, screen):
        return screen.blit(PLAYER, (self.rect.x - 44, self.rect.y))

    def hurt(self, die=False):
        self.die = die
        self.player_hp -= 1
        if self.player_hp == 0 or die:
            self.player_hp = 0
            explosion_sprites = pygame.sprite.Group()
            explosion = AnimatedSprite(load_image("exps.png", -1), 4, 4, self.rect.x - 70, self.rect.y - 40,
                                       explosion_sprites)
            for _ in range(16):
                explosion_sprites.update()
                explosion_sprites.draw(screen)
                pygame.time.wait(50)
                pygame.display.flip()
            if not(self.training):
                self.player_end.new_score(self.pl_score)

    def score(self, screen):
        cor_top = (150, 0)
        cor_wh = (130, 70)
        pygame.draw.rect(screen, (190, 80, 190), (cor_top, cor_wh))
        font = pygame.font.Font(None, 40)
        text = font.render(str(self.pl_score), True, pygame.Color('white'))
        screen.blit(text, (160, 20))




    def hearts(self):
        for i in range(self.player_hp):
            screen.blit(self.hp_image, (1000 + i * 36, 40))