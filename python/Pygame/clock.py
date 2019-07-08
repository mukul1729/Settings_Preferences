import pygame
import math
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
window.fill((255, 255, 255))
x, y = 0, 0

for a in range(270, 451, 6):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    x = 250 + 200 * math.cos((math.pi / 180) * a)
    y = 250 + 200 * math.sin((math.pi / 180) * a)
    window.fill((255, 255, 255))
    pygame.draw.line(window, (0, 0, 0), (250, 250), (x, y))
    clock.tick(1)
    pygame.display.update()
