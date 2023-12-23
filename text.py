import pygame
from threading import Timer

chislo = 100

def check():
    global chislo
    chislo -= 1
    print('1 second')
    Timer(1, check).start()

check()


pygame.init()
width, height = 500, 500

win = pygame.display.set_mode((width, height))

FPS = 60
clock = pygame.time.Clock()

font = pygame.font.Font('better-vcr-5.2.ttf', 36)


# 180, 0 ,0 - цвет


# 0, 0 корды

background = pygame.image.load('Volosatij_kolobok.png')
background = pygame.transform.scale(background, ((width, height)))
background2 = pygame.image.load('Vrode_bi_lisa.png')
background2 = pygame.transform.scale(background2, ((width, height)))
backgroundX1 = 0
backgroundX2 = background.get_rect().width

speed = 4
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.blit(background, (backgroundX1, 0))
    win.blit(background2, (backgroundX2, 0))
    backgroundX1 -= speed
    backgroundX2 -= speed
    if backgroundX1 == 0:
        backgroundX2 = background.get_rect().width
    if backgroundX2 == 0:
        backgroundX1 = background2.get_rect().width
    text = font.render('Число :' + str(chislo), True, (180, 0, 0))
    win.blit(text, (0, 0))
    pygame.display.update()
    clock.tick(FPS)