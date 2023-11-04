import pygame
import pygame as pg
import random
Gray = [70] * 3
Black = [0] * 3
White = [255] * 3
Wight, Height = 500, 500

pygame.init
win = pygame.display.set_mode((Wight, Height))

radius = 30
flag = 1
objtdr = 'Krug'
win.fill(White)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pos = pygame.mouse.get_pos()

    radius += flag
    if radius == 70:
        flag = -1
    elif radius == 30:
        flag = 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        objtdr = 'krug'
    elif keys[pygame.K_w]:
        objtdr = 'kvdr'
    elif keys[pygame.K_SPACE]:
        win.fill(White)
    if objtdr == 'krug':
        pygame.draw.circle(win,random.choices(range(0,256),k = 3),pos,radius)
    elif objtdr == 'kvdr':
        pygame.draw.rect(win,random.choices(range(0,256), k = 3),(pos[0] - 15, pos[1] - 15, radius, radius))

    pygame.display.update()
    pygame.time.delay(20)

