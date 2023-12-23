import random

import pygame

pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()

class Inginirium(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('Volosatij_kolobok.png')
        self.image = pygame.transform.scale(self.image, (140, 90))
        self.rect = self.image.get_rect()




    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.left -= 5
        elif keys[pygame.K_d]:
            self.rect.left += 5
        elif keys[pygame.K_w]:
            self.rect.top -= 5
        elif keys[pygame.K_s]:
            self.rect.top += 5




class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('Vrode_bi_lisa.png')
        self.image = pygame.transform.scale(self.image, (140, 90))
        self.rect = self.image.get_rect()
        self.healt = 50


    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.left += 5
        elif keys[pygame.K_UP]:
            self.rect.top-= 5
        elif keys[pygame.K_DOWN]:
            self.rect.top += 5

all_sprites = pygame.sprite.Group()
player = Inginirium(all_sprites)

                enemy.healt -= 1
                print(enemy.healt)
            else:
                enemy_sprites.remove(enemy)
        print('ДТП')

    pygame.sprite.Group()
    player = Inginirium(all_sprites)
    enemy_sprites = pygame.sprite.Group()
    Enemy(enemy_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        win.fill((255, 255, 255))
        all_sprites.draw(win)
        enemy_sprites.draw(win)
        enemy_sprites.update()
        all_sprites.update()
        for item in all_sprites:
            item.move_by_keys()
        for item in enemy_sprites:
            item.move_by_keys()
        hit = pygame.sprite.spritecollide(player, enemy_sprites, False)
        if len(hit) > 0:
            for enemy in hit:
                if enemy.healt > 1:
                    enemy.rect.left = random.randint(0, width)
                    enemy.rect.top = random.randint(0, height

    pygame.display.update()
    clock.tick(FPS)