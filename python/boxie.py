import pygame
pygame.init()

boxy = pygame.image.load('boxy.png')
slide1 = pygame.image.load('slide1.png')
window = pygame.display.set_mode((600, 600))
run = True

clock = pygame.time.Clock()
p1 = 0
x = 600
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((255, 255, 255))
    x = x - 1
    if x < -160:
        x = 600
    window.blit(slide1, (x, 536))
    window.blit(boxy, (284, 568 - p1))

    pygame.display.update()
    clock.tick(60)
