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
    pygame.draw.line(win,(255,255,255), (0,0), (width,height),5)
    pygame.draw.line(win,(255,255,255), (0,height), (width,0),5)
    pygame.display.set_caption('Дз.ЕхЕ')
    pygame.display.update()
