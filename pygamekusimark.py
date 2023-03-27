import pygame
import pygame as pg
from random import randint
from random import choice

#terve hunniks muutujaid
lopp=False
size= width, height= (800, 500)
skoor=0
elud=3
#tüüp:(värv) sinine; kollane; roheline, roosa, must, lilla
erinevad_kastid= {"normal":(190,250,255), "2xSkoor":(255,255,176), "0.5xK_Kiirus": (200, 255, 190), "2xK_Kiirus": (255, 192, 192), "mürgine":(61,61,61), "+1elu": (175,130,250)}
tüüp= choice(list(erinevad_kastid.keys()))
värv=erinevad_kastid[tüüp]
#kujund
a=30
tegelane=50
#kiirus
v_player= 10
v_kast=5
#kortinatid
x_player=width/2
y_player=height-tegelane
x_kast= randint(0,width)
y_kast=0

pg.init()
pygame.font.init()




#set up
pg.display.set_caption("suht lahe mäng")
gameplay= False
start= True
ded= False

aken0 = pygame.display.set_mode(size)
aken0.fill((200,200,200))
while start:
    pg.time.delay(10)
    aken0.fill((200,200,200))
    for event in pg.event.get():
        if event.type== pg.QUIT:
            start=False
    font = pygame.font.SysFont(None, 24)
    skoortekst = font.render("sa ei vajutaks tühikut >:|", True, "black")
    aken0.blit(skoortekst, (200, 250))
    keys=pg.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start=False
        gameplay= True

    pg.display.update()


aken = pygame.display.set_mode(size)
aken.fill((200,200,200))
#main mängu loop
while gameplay:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type== pg.QUIT:
            gameplay=False



    #mängija liikumine
    keys=pg.key.get_pressed()
    if keys[pygame.K_LEFT] and x_player>0:
        x_player-= v_player
    if keys[pygame.K_RIGHT] and x_player<width-tegelane:
        x_player+= v_player

    #kasti kukkumine
    if y_kast<550:
        y_kast+=v_kast
        v_kast+=0.001

    else:
        x_kast=randint(0,width-a)
        y_kast=0
        if tüüp!="mürgine":
            elud-=1
        lopp = True

    #kontrolli kas kukkus pähe v ei
    if y_player < (y_kast+tegelane):
        if ((x_player > x_kast and x_player < (x_kast + tegelane)) or ((x_player + tegelane) > x_kast and (x_player + tegelane) < (x_kast + tegelane))):

            #mässab skooriga
            if tüüp=="2xSkoor":
                skoor+=2
            elif tüüp=="2xK_Kiirus":
                skoor += 3
            elif tüüp=="0.5xK_Kiirus":
                skoor-=1
            elif tüüp=="+1elu":
                skoor-=1
            else:
                skoor+=1

            #muud efektid
            if tüüp =="0.5xK_Kiirus":
                v_kast=v_kast*0.5
            elif tüüp =="2xK_Kiirus":
                v_kast=v_kast*1.1
            elif tüüp=="mürgine":
                gameplay=False
            elif tüüp=="+1elu":
                elud+=1


            #reset
            x_kast=randint(0, width-a)
            y_kast=0
            lopp=True

        if elud==0:
            gameplay=False
            ded=True

#joonistame
    aken.fill((200,200,200))
    pg.draw.rect(aken, (100,150,150), (x_player, y_player, tegelane, tegelane))

#tegelintski
    pg.draw.rect(aken, värv, (x_kast, y_kast, a, a))

#kiri
    font = pygame.font.SysFont(None, 24)
    skoortekst = font.render("skoor: " + str(skoor), True, "black")
    aken.blit(skoortekst, (20, 20))
    elutekst = font.render("elu: " + str(elud), True, "black")
    aken.blit(elutekst, (20, 50))
    pg.display.update()

    if lopp== True:
        tüüp = choice(list(erinevad_kastid.keys()))
        värv = erinevad_kastid[tüüp]
        lopp=False


aken2 = pygame.display.set_mode(size)
aken2.fill((200,200,200))
#game over
while ded:
    pg.time.delay(10)
    loser = font.render("HAH NOOB OLED!!!!!!!!!!!", True, "black")
    aken2.blit(loser, (200, 250))
    for event in pg.event.get():
        if event.type== pg.QUIT:
            ded= False
    pg.display.update()





pygame.quit()

