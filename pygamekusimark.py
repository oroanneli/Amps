import pygame
import pygame as pg
from random import randint
from random import choice

#terve hunniks muutujaid
size= width, height= (800, 500)
skoor=0
#tüüp:(värv) sinine; kollane; roheline, roosa
erinevad_kastid= {"normal":(190,250,255), "2xSkoor":(255,255,176), "0.5xK_Kiirus": (200, 255, 190), "2xK_Kiirus": (255, 192, 192)}
tüüp= choice(list(erinevad_kastid.keys()))
värv=erinevad_kastid[tüüp]
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
pg.display.set_caption("suht lahe mäng")
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

    #kasti kukkumine
    if y_kast<500:
        y_kast+=v_kast
        v_kast+=0.001
    else:
        x_kast=randint(0,width-a)
        y_kast=0

    #kontrolli kas kukkus pähe v ei
    if y_player < (y_kast+a):
        if ((x_player > x_kast and x_player < (x_kast + a)) or ((x_player + a) > x_kast and (x_player + a) < (x_kast + a))):
            if tüüp=="2xSkoor":
                skoor+=2
            else:
                skoor+=1
            if tüüp =="0.5xK_Kiirus":
                v_kast=v_kast*0.5
            elif tüüp =="2xK_Kiirus":
                v_kast=v_kast*1.1

            #reset
            x_kast=randint(0,width-a)
            y_kast=0
        tüüp= choice(list(erinevad_kastid.keys()))
        värv=erinevad_kastid[tüüp]




#joonistame
    aken.fill((200,200,200))
    pg.draw.rect(aken, (100,150,150), (x_player, y_player, a, a))

#tegelintski
    pg.draw.rect(aken, värv, (x_kast, y_kast, a, a))

#kiri
    font = pygame.font.SysFont(None, 24)
    txt = font.render("skoor: " + str(skoor), True, "black")
    aken.blit(txt, (20, 20))
    pg.display.update()





pygame.quit()

