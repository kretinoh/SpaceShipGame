'''
Aprendiendo python con libreria pygame
Siguiendo tutorial de https://github.com/techwithtim

Juego para dos jugadores en local donde manejas tu propia nave e intentas
eliminar a tu enemigo

TODO Disparos de las naves, colision de proyectiles, vida, hud
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

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 3 # Velocidad a la que se moverán las naves

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Pygame', 'Assets/spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Pygame', 'Assets/spaceship_red.png'))
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


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

# pop-up
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # EVENTO POR EL CUAL CERRAMOS LA VENTANA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


# Con esta linea conseguimos hacer que se ejecute el main solo si se llama a este archivo
# y evitamos que se ejecute al importarlo
if __name__ == "__main__":
    main()