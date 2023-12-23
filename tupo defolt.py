import pygame

pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
