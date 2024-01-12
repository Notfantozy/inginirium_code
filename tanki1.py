import pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32

DIRS = [[0, -1], [1, 0], [0, -1], [-1, 0]]

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Tank:
    def __init__(self, color, gx, gy, dir, key1):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(gx, gy, TILE, TILE)
        self.dir = dir
        self.moveSpeed = 2
        self.hp = 5

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.keyLEFT = key1[0]
        self.keyRIGHT = key1[1]
        self.keyUP = key1[2]
        self.keyDOWN = key1[3]
        self.keySHOT = key1[4]

    def update(self):
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.dir = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.dir = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.dir = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.dir = 2

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRS[self.dir][0] * self.bulletSpeed
            dy = DIRS[self.dir][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

        x = self.rect.centerx + DIRS[self.dir][0] * 30
        y = self.rect.centery + DIRS[self.dir][1] * 30
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
            print(self.color, 'Dead :(')

class Bullet:
    def __init__(self, parent, gx, gy, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.gx, self.gy = gx, gy
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.gx += self.dx
        self.gy += self.dy

        if self.gx < 0 or self.gx > WIDTH or self.gy < 0 or self.gy > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.gx, self.gy):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break
    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.gx, self.gy), 2)

bullets = []
objects = []
Tank('blue', 100, 275 , 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_LSHIFT))
Tank('green', 700, 275 , 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    for bullet in bullets: bullet.update()
    for obj in objects: obj.update()

    window.fill('black')
    for bullet in bullets: bullet.draw()
    for obj in objects: obj.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()