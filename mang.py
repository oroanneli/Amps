import pygame as pg

pg.init()

aken= pg.display.set_mode((800,400))
run=True
x=0
y=0

player= pg.image.load("pildid\pilt1.jpg").convert_alpha()

while run:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                x+=10

    aken.fill((255,255,255))
    aken.blit(player, (x, y))
    #x+=1
    pg.display.flip()


