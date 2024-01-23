
import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fontUI = pygame.font.Font(None, 30)

imgBrick = pygame.image.load('images/block_brick.png')
imgTanks = pygame.image.load('images/tank1.png'),
imgBangs = [
    pygame.image.load('images/bang1.png'),
    pygame.image.load('images/bang2.png'),
    pygame.image.load('images/bang3.png'),
    ]


DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class UI:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.hp), 1, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                i += 1


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

        self.rank = 0
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.dir * 90)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.dir * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center=self.rect.center)

        oldX, oldY = self.rect.topleft
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

        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRS[self.dir][0] * self.bulletSpeed
            dy = DIRS[self.dir][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        window.blit(self.image, self.rect)

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
                if obj != self.parent and obj.type != 'bang' and obj.rect.collidepoint(self.gx, self.gy):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.gx, self.gy)
                    break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.gx, self.gy), 2)


class Bang:
    def __init__(self, gx, gy):
        objects.append(self)
        self.type = 'bang'

        self.gx, self.gy = gx, gy
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3: objects.remove(self)

    def draw(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center = (self.gx, self.gy))
        window.blit(image, rect)

class Block:
    def __init__(self, gx, gy, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(gx, gy, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        window.blit(imgBrick, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: objects.remove(self)



bullets = []
objects = []
Tank('blue', 100, 275 , 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_LSHIFT))
Tank('green', 700, 275 , 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL))
ui = UI()

for build in range(50):
    while True:
        x = randint(0, WIDTH // TILE -2) * TILE
        y = randint(1, HEIGHT // TILE - 2) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fin = False
        for obj in objects:
            if rect.colliderect(obj.rect): fined = True

        if not fin: break

    Block(x, y, TILE)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    for bullet in bullets: bullet.update()
    for obj in objects: obj.update()
    ui.update()

    window.fill('black')
    for bullet in bullets: bullet.draw()
    for obj in objects: obj.draw()
    ui.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
