import pygame
import pygame as pg
from random import randint

#terve hunniks muutujaid
size= width, height= (800, 500)
skoor=0


#kujund
a=30

#kiirus
v_player= 10
v_kast=5
#kortinatid
x_player=width/2
y_player=height-a
x_kast= randint(0,width)
y_kast=0

pg.init()
pygame.font.init()

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

    #mängija liikumine
    keys=pg.key.get_pressed()
    if keys[pygame.K_LEFT] and x_player>0:
        x_player-= v_player
    if keys[pygame.K_RIGHT] and x_player<width-a:
        x_player+= v_player

    if y_kast<500:
        y_kast+=v_kast
        v_kast+=0.001
    else:
        x_kast=randint(0,width-a)
        y_kast=0
    if y_player < (y_kast+a):
        if ((x_player > x_kast and x_player < (x_kast + a)) or ((x_player + a) > x_kast and (x_player + a) < (x_kast + a))):
            skoor+=1
            x_kast=randint(0,width-a)
            y_kast=0



#joonistame
    aken.fill((200,200,200))
    pg.draw.rect(aken, (100,150,150), (x_player, y_player, a, a))

#tegelintski
    pg.draw.rect(aken,(0, 255, 255), (x_kast, y_kast, a, a))
    font = pygame.font.SysFont(None, 24)
    img = font.render("skoor: " + str(skoor), True, "black")
    aken.blit(img, (20, 20))
    pg.display.update()





pygame.quit()

