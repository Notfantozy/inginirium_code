import pygame
pygame.init()
win = pygame.display.set_mode((1920,1080))


class circl():
    def __init__(self, win, color, x, y, rad):
        self.color = color
        self.win = win
        self.x = x
        self.y = y
        self.rad = rad
    def draw(self):
        pygame.draw.circle(win,(self.color), (self.x, self.y), self.rad)
    def move_by_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.x += 1
        elif keys[pygame.K_UP]:
            self.y -= 1
        elif keys[pygame.K_DOWN]:
            self.y += 1kryg.draw()



x = 10
y = 10
rad = 306

kryg = circl(win, (0, 255, 0), 10, 20, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    kryg.draw()
    kryg.move_by_key()
    pygame.display.update()
