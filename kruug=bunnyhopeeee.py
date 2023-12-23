import pygame
pygame.init()
win = pygame.display.set_mode((1920,1030))
FPS = 60
Clock = pygame.time.Clock()



class circl():
    def __init__(self, win, color, x, y, rad):
        self.color = color
        self.win = win
        self.x = x
        self.y = y
        self.rad = rad
        self.isJump = False
        self.jump_counter = 30

    def draw(self):
        pygame.draw.circle(win,(self.color), (self.x, self.y), self.rad)

    def move_by_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.x += 5
        elif keys[pygame.K_UP]:
            self.y -= 5
        elif keys[pygame.K_DOWN]:
            self.y += 5
        elif keys[pygame.K_SPACE]:
            self.isJump = True

        if self.isJump:
            if self.jump_counter >= -30:
                self.y -= self.jump_counter
                self.jump_counter -= 2

            else:
                self.jump_counter = 30
                self.isJump = False



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
    Clock.tick(FPS)