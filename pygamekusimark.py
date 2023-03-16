import pygame
import pygame as pg
from random import randint

#terve hunniks muutujaid
size= width, height= (800, 500)
#kujund
a=30
b=30
#kiirus
v= 5
#kortinatid
x_player=width/2
y_player=height-b
x_kast= randint(0,280)
y_kast=0

pg.init()

#set up
aken = pygame.display.set_mode(size)
pg.display.set_caption("jah?")
gameplay= True

#mängu loop
while gameplay:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type== pg.QUIT:
            gameplay=False

    keys=pg.key.get_pressed()
    if keys[pygame.K_LEFT] and x_player>0:
        x_player-= v
    if keys[pygame.K_RIGHT] and x_player<width-a:
        x_player+= v
    if y_kast<500:
        y_kast+=5
    else:
        y_kast=0
        x_kast=randint(0,280)

    #joonistame
    aken.fill((200,200,200))
    pg.draw.rect(aken, (100,150,150), (x_player, y_player, a, b))

#tegelintski
    pg.draw.rect(aken,(0, 255, 255), (x_kast, y_kast, a, b))
    pg.display.update()





pygame.quit()

