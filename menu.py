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


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surf = pygame.Surface((width // 2, height))
        self.surf.fill((200, 200, 200, 30))
        self.menu_ok = True
        self.wh_but = 240, 80
        self.but_up = (181, 181, 181)


    def draw_but1(self):
        pygame.draw.rect(self.surf, self.but_up, ((170, 270), self.wh_but))
        font = pygame.font.Font(None, 40)
        text = font.render("Продолжить", True, pygame.Color('black'))
        self.surf.blit(text, (200, 300))

    def draw_but2(self):
        pygame.draw.rect(self.surf, self.but_up, ((170, 370), self.wh_but))
        font = pygame.font.Font(None, 40)
        text = font.render("Заново", True, pygame.Color('black'))
        self.surf.blit(text, (240, 400))

    def draw_but3(self):
        pygame.draw.rect(self.surf, self.but_up, ((170, 470), self.wh_but))
        font = pygame.font.Font(None, 40)
        text = font.render("Выйти", True, pygame.Color('black'))
        self.surf.blit(text, (245, 500))



    def go_menu(self, screen):
        cursor_pos = None
        while self.menu_ok:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == 105:
                        self.menu_ok = False
                if event.type == pygame.MOUSEMOTION:
                    cursor_pos = event.pos
                if pygame.mouse.get_focused() and cursor_pos:
                    if 470 <= cursor_pos[0] <= 610:
                        if 270 <= cursor_pos[1] <= 350:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                self.menu_ok = False

            screen.blit(self.surf, (self.width // 4, 0))
            self.draw_but1()
            self.draw_but2()
            self.draw_but3()
            pygame.display.flip()