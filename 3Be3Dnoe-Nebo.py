import pygame as pg
import random

Gray = [70] * 3
Black = [0] * 3
White = [255] * 3
W, H = 800, 800
pg.init()
win = pg.display.set_mode((W, H))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    for i in  range(10):
        pg.draw.circle(win, Gray, \
                       (random.randint(0, W), random.randint(0, H)), 1)
    pressed = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()
    if keys[pg.K_l]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, White, pos, 40)
    if pressed[2]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, Black, pos, 10)
    if pressed[1]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, Gray, pos, 1)
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, White, pos, 5)
    pg.display.update()


    pg.time.delay(20)
