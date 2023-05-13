width = int(input("Числo1:"))
height = int(input("Числo2:"))
import pygame
pygame.init()
win = pygame.display.set_mode((width, height))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #win.fill(color)
    pygame.draw.line(win,(255,255,255), (width,height), (100,100),5)
    pygame.draw.line(win,(255,255,255), (width,height), (100,100),5)
    pygame.display.update()
