'''
Aprendiendo python con libreria pygame
Siguiendo tutorial de https://github.com/techwithtim

Juego para dos jugadores en local donde manejas tu propia nave e intentas
eliminar a tu enemigo

TODO  hud
@author: kretinoh
'''
import pygame
import os

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

# CONSTANTES
pygame.display.set_caption("Space Ships!")
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 3 # Velocidad a la que se moverán las naves
BULLET_VEL = 7
MAX_BULLETS = 4
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT =pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

def yellow_handle_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # DOWN
            yellow.y += VEL

def red_handle_movement(keys_pressed, red):
        if keys_pressed[K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # LEFT
            red.x -= VEL
        if keys_pressed[K_RIGHT] and red.x + VEL + red.width < WIDTH: # RIGHT
            red.x += VEL
        if keys_pressed[K_UP] and red.y - VEL > 0: # UP
            red.y -= VEL
        if keys_pressed[K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # DOWN
            red.y += VEL


def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

# pop-up
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # EVENTO POR EL CUAL CERRAMOS LA VENTANA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets)

    pygame.quit()


# Con esta linea conseguimos hacer que se ejecute el main solo si se llama a este archivo
# y evitamos que se ejecute al importarlo
if __name__ == "__main__":
    main()