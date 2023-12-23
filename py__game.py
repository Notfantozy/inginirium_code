import pygame
pygame.init()
width = 500
height = 500

win = pygame.display.set_mode((width, height))
color = (255,255,255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(color)
    pygame.draw.rect(win,(255,255,0), (50,30,30,0))
    pygame.draw.circle(win,(0,255,255),(50,20), 50)
    pygame.draw.polygon(win, (0,0,0),[(0,100),(100,50), (100,150)], False)
    pygame.draw.line(win,(0,255,255), (0,0), (100,100),5)
    pygame.draw.lines(win, (0,0,0), True, ((200,200),(300,150), (300,250)))
    pygame.display.update()