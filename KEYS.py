import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
x = 250
y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=0.1
    elif keys[pygame.K_RIGHT]:
        x+=0.1
    elif keys[pygame.K_UP]:
        y-=0.1
    elif keys[pygame.K_DOWN]:
        y+=0.1
    win.fill((255, 255, 255))  
    pygame.draw.circle(win, (255, 103, 11), (x, y), 30)

    pygame.display.update()