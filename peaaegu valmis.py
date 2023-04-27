    
import pygame
import pygame as pg
from random import randint
from random import choices

#terve hunniks muutujaid
lopp=False
skoor=0
elud=3

size= width, height= (800, 500)
aken = pygame.display.set_mode(size)

#taustapilt
taust = pg.image.load("taust.png")
taust = pg.transform.scale(taust,(width,height)).convert_alpha()

lõpp = pg.image.load("lõpp.png")
lõpp = pg.transform.scale(lõpp,(width,height)).convert_alpha()
#sõõrikute pildid (et oleks õige suurusega)
sinine = pg.transform.scale(pg.image.load("sinine.png"),(110,110))
kollane= pg.transform.scale(pg.image.load("kollane.png"),(110,110))
lilla = pg.transform.scale(pg.image.load("lilla.png"),(110,110))
roheline = pg.transform.scale(pg.image.load("roheline.png"),(110,110))
roosa = pg.transform.scale(pg.image.load("roosa.png"),(110,110))
myrgine = pg.transform.scale(pg.image.load("radioaktiivne.png"),(110,110))




#taustamuusika
pg.mixer.init()
muusika = pg.mixer.music.load("taust.mp3")
#heliefektid
püüdis = pg.mixer.Sound("sõõrik.wav")
läbi = pg.mixer.Sound("läbi.wav")

#tüüp:(värv) normal=sinine; 2xskoor=kollane; 0.5xKiirus=roheline, 2xKiirus=roosa, mürgine=must, +1elu=lilla
erinevad_soorikud= {"normal":sinine, "2xSkoor":kollane, "0.5xK_Kiirus": roheline, "2xK_Kiirus": roosa, "mürgine":myrgine, "+1elu": lilla}

#tüüp= ["normal", "2xSkoor", "0.5xK_Kiirus", "2xK_Kiirus", "mürgine", "+1elu"]

tüüp= choices(list(erinevad_soorikud.keys()), weights=(4,3,3,3,2,1), k=1)
tüüp=tüüp[0]
värv=erinevad_soorikud[tüüp]
#kujund
sooriku_laius = 80
tegelane=90
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
pg.display.set_caption("Taevast sajab sõõrikuid")
gameplay= False
start= True
ded= False
pelu=True


while start:
    pg.time.delay(10)
    aken.blit(taust,(0,0))
    for event in pg.event.get():
        if event.type== pg.QUIT:
            start=False
            pelu=False
    font = pygame.font.SysFont(None, 24)
    #kuritekst = font.render("sa ei vajutaks tühikut >:|", True, "black")
    # tüüp:(värv) normal=sinine; 2xskoor=kollane; 0.5xKiirus=roheline, 2xKiirus=roosa, mürgine=must, +1elu=lilla
    tutorialtekst=font.render("liikumiseks: < > ; [tühik] et alustada", True, "black")
    tutorialtekst1=font.render("mugi sõõrikuid a mustast hoia eemale", True, "black")
    tutorialtekst2=font.render("sinine: +1 skoor, kollane: +2 skoor, roheline: -kiirus - skoor, roosa: +kiirus +3 skoor", True, "black")


    #aken.blit(kuritekst, (200, 250))
    aken.blit(tutorialtekst1, (150, 100))
    aken.blit(tutorialtekst2, (150, 300))

    aken.blit(tutorialtekst, (150, 400))
    keys=pg.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start=False
        pelu= True
        gameplay=True

    pg.display.update()

for event in pg.event.get():
    if event.type == pg.QUIT:
        pelu = False

while pelu:
    pg.mixer.music.play(-1) #muusika mängib loopis

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pelu = False 
    #main mängu loop
    while gameplay:

        if elud <= 0:
            gameplay = False
            ded = True

        pg.time.delay(10)
        for event in pg.event.get():
            if event.type== pg.QUIT:
                gameplay=False
                pelu=False



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
            x_kast=randint(0,width-sooriku_laius)
            y_kast=0
            if tüüp!="mürgine":
                elud-=1
            lopp = True


        #kontrolli kas kukkus pähe v ei
        if y_player < (y_kast+tegelane):
            if ((x_player > x_kast and x_player < (x_kast + tegelane)) or ((x_player + tegelane) > x_kast and (x_player + tegelane) < (x_kast + tegelane))):
                püüdis.play()

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
                    ded=True
                elif tüüp=="+1elu":
                    elud+=1


                #reset
                x_kast=randint(0, width-sooriku_laius)
                y_kast=0
                lopp=True

    #joonistame
        aken.blit(taust,(0,0))
        püüdja = pg.transform.scale(pg.image.load("krok.png"),(90,90))
        aken.blit(püüdja,(x_player,y_player))

    #tegelintski

        aken.blit(värv,(x_kast, y_kast))

    #kiri
        font = pygame.font.SysFont(None, 24)
        skoortekst = font.render("SKOOR: " + str(skoor), True, "black")
        aken.blit(skoortekst, (20, 20))
        elutekst = font.render("ELU: " + str(elud), True, "black")
        aken.blit(elutekst, (20, 50))
        pg.display.update()

        if lopp== True:
            tüüp= choices(list(erinevad_soorikud.keys()), weights=(4,3,3,3,2,1), k=1)
            tüüp=tüüp[0]
            värv=erinevad_soorikud[tüüp]
            lopp=False


    aken.blit(lõpp,(0,0))
    #game over
    if  ded:
        pg.mixer.music.stop() #muusika lõpetab
        läbi.play() #mängib end soundi
    while ded:
        pg.time.delay(10)
        loser = font.render("HAH NOOB OLED!!!!!!!!!!!", True, "black")
        aken.blit(loser, (200, 250))
        for event in pg.event.get():
            if event.type== pg.QUIT:
                ded= False
                pelu=False
        keys = pg.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ded = False
            gameplay = True
            elud=3
            skoor = 0
        pg.display.update()






pg.quit()
