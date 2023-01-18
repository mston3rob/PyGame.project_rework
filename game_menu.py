import pygame
import sys


pygame.init()
clock = pygame.time.Clock()

class Game_Menu:
    def __init__(self, width, height, FPS):
        self.width = width
        self.height = height
        self.surf = pygame.Surface((width // 3, height))
        self.surf.fill((200, 200, 200, 30))
        self.menu_ok = True
        self.wh_but = 240, 80
        self.but_up = (181, 181, 181)
        self.FPS = FPS

    def draw_but1(self):
        pygame.draw.rect(self.surf, self.but_up, ((140, 270), self.wh_but))
        font = pygame.font.Font(None, 40)
        text = font.render("Начать игру", True, pygame.Color('black'))
        self.surf.blit(text, (200, 300))

    def draw_but2(self):
        pygame.draw.rect(self.surf, self.but_up, ((140, 370), self.wh_but))
        font = pygame.font.Font(None, 40)
        text = font.render("Обучение", True, pygame.Color('black'))
        self.surf.blit(text, (210, 400))

    def draw_but3(self):
        pygame.draw.rect(self.surf, self.but_up, ((140, 470), self.wh_but))
        font = pygame.font.Font(None, 40)
        text = font.render("Выйти", True, pygame.Color('black'))
        self.surf.blit(text, (220, 500))

    def go__game_menu(self, screen):
        cursor_pos = None
        while self.menu_ok:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    cursor_pos = event.pos
                if pygame.mouse.get_focused() and cursor_pos:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 940 <= cursor_pos[0] <= 1080:
                            if 270 <= cursor_pos[1] <= 350:
                                return 0
                            elif 370 <= cursor_pos[1] <= 450:
                                return 1
                            elif 470 <= cursor_pos[1] <= 550:
                                return 2
            screen.blit(self.surf, (self.width // 3 * 2, 0))
            self.draw_but1()
            self.draw_but2()
            self.draw_but3()
            pygame.display.flip()
            clock.tick(self.FPS)