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

    def draw_but_to_menu(self, screen):
        cor_top = (0, 0)
        cor_wh = (130, 70)
        pygame.draw.rect(screen, (190, 80, 190), (cor_top, cor_wh))
        pygame.draw.rect(screen, (90, 40, 90), (cor_top, cor_wh), 3)
        font = pygame.font.Font(None, 40)
        text = font.render("Выйти", True, pygame.Color('white'))
        screen.blit(text, (20, 20))



    def go_menu(self, screen):
        cursor_pos = None
        while self.menu_ok:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_ok = False
                        return 2, True
                if event.type == pygame.MOUSEMOTION:
                    cursor_pos = event.pos
                if pygame.mouse.get_focused() and cursor_pos:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 470 <= cursor_pos[0] <= 710:
                            if 270 <= cursor_pos[1] <= 350:
                                self.menu_ok = False
                                return 2, True
                            elif 370 <= cursor_pos[1] <= 450:
                                return 1, False
                            elif 470 <= cursor_pos[1] <= 550:
                                return 0, False
                        if 0 <= cursor_pos[0] <= 130 and 0 <= cursor_pos[1] <= 70:
                            self.menu_ok = False
                            return 2, True

            screen.blit(self.surf, (self.width // 4, 0))
            self.draw_but1()
            self.draw_but2()
            self.draw_but3()
            pygame.display.flip()