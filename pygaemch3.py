import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
x = 250
y = 250
speed = 3
color = (255, 0, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=speed
    elif keys[pygame.K_RIGHT]:
        x+=speed
    elif keys[pygame.K_UP]:
        y-=speed
    elif keys[pygame.K_DOWN]:
        y+=speed
    else:
        x = 250
        y = 250
    win.fill((255, 255, 255))
    color = (255,0,255)
    if x - 150> 250:
        color = (255,0,0)
        speed = 1
    if x + 150< 250:
        color = (255,0,0)
        speed = 1
    if y - 150> 250:
        color = (255,0,0)
        speed = 1
    if y + 150< 250:
        color = (255,0,0)
        speed = 1
    else:
        speed = 3
    pygame.draw.circle(win, color, (x, y), 30)

    pygame.display.update()
    pygame.time.delay(10)
    print(x)