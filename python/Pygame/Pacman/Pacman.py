import pygame
import math
import random
pygame.init()
window = ((512, 512))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
snake = ((200, 200), (220, 220))
clock = pygame.time.Clock()
disp = pygame.display.set_mode(window)
x = 200
y = 200
dir = 0
x_change = 0
y_change = 0
pacman_right = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/pacman_right.gif')
pacman_left = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/pacman_left.gif')
pacman_up = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/pacman_up.gif')
pacman_down = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/pacman_down.gif')
background = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/dot.gif')
wall = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/wall.gif')
monster = pygame.image.load(
    'E:/Programming/SH/python/Pygame/Pacman/pacman/monster1.gif')

p = random.randint(0, 400)
q = random.randint(0, 400)


def back():
    for x1 in range(0, 512, 32):
        for y1 in range(0, 512, 32):
            disp.blit(background, (x1, y1))
            if x1 == 0 and y1 >= 0 or x1 >= 0 and y1 == 0 or x1 >= 480 and y1 >= 0 or y1 >= 480 and x1 >= 0:
                disp.blit(wall, (x1, y1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = - 2
                y_change = 0
                dir = 1

            if event.key == pygame.K_RIGHT:
                x_change = 2
                y_change = 0
                dir = 2
            if event.key == pygame.K_UP:
                y_change = - 2
                x_change = 0
                dir = 3
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 2
                dir = 4
    x = x + x_change
    y = y + y_change
    back()
    if x <= 32 or x >= 448:
        x_change = 0
    if y <= 32 or y >= 448:
        y_change = 0

    if dir == 1:
        disp.blit(pacman_left, (x, y))
    if dir == 2:
        disp.blit(pacman_right, (x, y))
    if dir == 3:
        disp.blit(pacman_up, (x, y))
    if dir == 4:
        disp.blit(pacman_down, (x, y))
    block_x = math.floor(x / 32)
    block_y = math.floor(y / 32)

    disp.blit(monster, (p, q))

    pygame.display.update()
    clock.tick(100)
