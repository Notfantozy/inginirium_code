import  pygame

pygame.init()
size = w, h = 700, 700
fps = 30
win = pygame.display.set_mode(size)

img = pygame.image.load('ing.png')
img = img.convert()
colorkey = img.get_at((0, 0))
img.set_colorkey(colorkey)


img1 = pygame.transform.scale(img, (700, 700))
img2 = pygame.transform.scale(img, (700, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    win.blit(img, (0, 0))
    win.blit(img1,(100, 100))
    win.blit(img2, (200, 200))
    pygame. display.update()