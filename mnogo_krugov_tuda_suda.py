import random

import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
FPS = 60
Clock = pygame.time.Clock()



class Circle():
    def __init__(self, x, y, rad, color):
        self.color = color
        self.win = win
        self.x = x
        self.y = y
        self.rad = rad
        self.dir = 'right'


    def draw(self):
        pygame.draw.circle(win,self.color, (self.x, self.y), self.rad)
    def zmey(self):
        if self.dir == 'right':
            self.x += 7
            if self.x >=500:
                self.dir = 'left'
        else:
            self.x -= 7
            if self.x <= 0:
                self.dir = 'right'





x = 10
y = 10
rad = 306


list_circles = []
for i in range(100):
    list_circles.append(Circle(i*10, i * 5, 30,random.choices(range(256),k = 3)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,255,255))
    for i in range(100):
        list_circles[i].draw()
        list_circles[i].zmey()
    pygame.display.update()
    Clock.tick(FPS)