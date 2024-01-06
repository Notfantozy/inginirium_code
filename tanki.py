import pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32


window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Tank:
    def __init__(self, color, x, y, dir, key1):
        objects.append(self)
        self.type = 'tank'
        self.color = color
        self.rect = pygame.Rect(x, y, TILE, TILE)
        self.dir = dir
        self.moveSpeed = 1

        self.keyLEFT = key1[0]
        self.keyRIGHT = key1[1]
        self.keyUP = key1[2]
        self.keyDOWN = key1[3]
        self.keySHOT = key1[4]

    def update(self):
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed


    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


objects = []
Tank('blue', 100, 275 , 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    for obj in objects: obj.update()

    window.fill('black')
    for obj in objects: obj.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()