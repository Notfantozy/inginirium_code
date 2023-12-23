import pygame as pg
import random
pos = 250, 250
W, H = 500, 500
pg.init()
win = pg.display.set_mode((W, H))
def random_color():
    x = random.randint(0,255)
    n = random.randint(0,255)
    g = random.randint(0,255)
    return (x,n,g)

color = random_color()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    for i in  range(10):
        pg.draw.circle(win,color,(pos),30,30,30)

    pg.display.update()