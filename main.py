import pygame
import os
import sys
import random
from meteors import Meteor
from shells import Shells
from player import Player
from menu import Menu
from game_menu import Game_Menu

# инициалитзация pygame для работы со спрайтами и загрузкой изображения
pygame.init()
size = WIDTH, HEIGHT = 1200, 840
# ширина экрана должна быть кратна фреймрету (FPS)
screen = pygame.display.set_mode(size)
# инициализация спрайтов метеоритов
meteorites = pygame.sprite.Group()
particles = pygame.sprite.Group()
shells = pygame.sprite.Group()
FPS = 60
clock = pygame.time.Clock()
g_m = Game_Menu(WIDTH, HEIGHT, FPS)


def game():
    SHOT_TIMING = pygame.USEREVENT + 1
    CHANGE_DIFFICULT = pygame.USEREVENT + 2
    difficult = 1
    diff_was_changed = False
    fire_rate = 200
    shells_velocity = 10
    score = 0


    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        running, shooting, stop = True, False, False
        cursor_pos = None
        to_g_menu = 2
        player = Player()
        menu = Menu(WIDTH, HEIGHT, FPS)
        pygame.time.set_timer(CHANGE_DIFFICULT, 20000)
        pygame.time.set_timer(SHOT_TIMING, fire_rate)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        stop = True
                if event.type == pygame.QUIT:
                    running = False
                if not stop:
                    if event.type == pygame.MOUSEMOTION:
                        cursor_pos = event.pos
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        shooting = True
                    if event.type == pygame.MOUSEBUTTONUP:
                        shooting = False
                    if event.type == SHOT_TIMING and shooting:
                        Shells(shells, pos=(player.get_pos()), velocity=shells_velocity)
                    if pygame.mouse.get_focused() and cursor_pos:
                        if 0 <= cursor_pos[0] <= 130 and 0 <= cursor_pos[1] <= 70:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                stop = True
                    if event.type == CHANGE_DIFFICULT:
                        difficult += 1
                        diff_was_changed = False
            if stop:
                to_g_menu, running = menu.go_menu(screen)
                menu.menu_ok, stop = True, False
            else:
                if difficult == 1:
                    if len(meteorites) < 1:
                        Meteor(meteorites, vy=random.randint(1, 2))
                elif difficult == 2:
                    if len(meteorites) < 2:
                        if len(meteorites) < 1:
                            Meteor(meteorites, vy=random.randint(1, 3))
                        else:
                            if random.randint(1, 50) == 2:
                                Meteor(meteorites, vy=random.randint(1, 3))
                elif difficult == 3:
                    if len(meteorites) < 2:
                        if len(meteorites) < 1:
                            Meteor(meteorites, vy=random.randint(1, 4))
                        else:
                            if random.randint(1, 50) == 2:
                                Meteor(meteorites, vy=random.randint(1, 4))
                elif difficult == 4:
                    if not diff_was_changed:
                        fire_rate = 200
                        pygame.time.set_timer(SHOT_TIMING, fire_rate)
                        diff_was_changed = True
                        print(11)
                    if len(meteorites) < 3:
                        if len(meteorites) < 1:
                            Meteor(meteorites, vy=random.randint(1, 4))
                        else:
                            if random.randint(1, 40) == 2:
                                Meteor(meteorites, vy=random.randint(1, 4))
                elif difficult == 5:
                    if not diff_was_changed:
                        fire_rate = 160
                        pygame.time.set_timer(SHOT_TIMING, fire_rate)
                        diff_was_changed = True
                        print(11)
                    if len(meteorites) < 3:
                        if len(meteorites) < 1:
                            Meteor(meteorites, vy=random.randint(1, 5))
                        else:
                            if random.randint(1, 40) == 2:
                                Meteor(meteorites, vy=random.randint(1, 5))

                elif difficult >= 6:
                    if not diff_was_changed:
                        fire_rate = 160
                        shells_velocity = 15
                        pygame.time.set_timer(SHOT_TIMING, fire_rate)
                        diff_was_changed = True
                        print(11)
                    if len(meteorites) < 4:
                        if len(meteorites) < 1:
                            Meteor(meteorites, vy=random.randint(1, 5))
                        else:
                            if random.randint(1, 40) == 2:
                                Meteor(meteorites, vy=random.randint(1, 5))

                screen.fill(pygame.Color('Black'))
                if pygame.mouse.get_focused() and cursor_pos:
                    player.update(cursor_pos[0])
                player.draw(screen)
                shells.draw(screen)
                shells.update(meteorites)
                meteorites.draw(screen)
                meteorites.update(shells, meteorites, particles, player)
                particles.draw(screen)
                particles.update()
                player.hearts()
                menu.draw_but_to_menu(screen)
                clock.tick(FPS)
            pygame.display.flip()
        if to_g_menu == 0 or to_g_menu == 1:
            for i in meteorites:
                i.kill()
            for i in shells:
                i.kill()
            for i in particles:
                i.kill()
            if to_g_menu == 0:
                game_menu()
            else:
                game()
        else:
            pygame.quit()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

FON = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))

def game_menu():
    screen.blit(FON, (0, 0))
    pygame.display.flip()
    game_pos = g_m.go__game_menu(screen)
    if game_pos == 0:
        game()
    if game_pos == 1:
        pass
    if game_pos == 2:
        terminate()


def start_screen():
    intro_text = ["Добро пожаловать", "",
                  "Правила игры",
                  "Уничтожь все метеориты,",
                  "чтобы спасти планету"]
    screen.blit(FON, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    load = True
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while load:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                game_menu()
                load = False
        if load:
            pygame.display.flip()
            clock.tick(FPS)
start_screen()