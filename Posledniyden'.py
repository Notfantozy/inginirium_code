import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
x = 100
y = 50
k = 0
d = 0
h=500
l=500
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = x + 1
    win.fill((255,255,255))
    pygame.draw.rect(win,(255, 255, 0), (x, 50, 100, 150))


    if x == 500:
        x = 0
    y= y+1
    k= k+1
    d= d+1
    h= h-1
    l= l-1
    pygame.draw.circle(win, (255,103,11), (100, y), 50)
    pygame.draw.circle(win, (255, 210, 74), (k, d), 50)
    pygame.draw.circle(win, (255, 103, 11), (h, l), 50)
    pygame.display.update()
    if y == 500:
        y = 0
    pygame.time.delay(10)
