import pygame
import pygame as pg
from random import randint

size= width, height= (300, 500)
x=width/2
xk= randint(0,280)
y=0

pg.init()

#set up
aken = pygame.display.set_mode(size)
pg.display.set_caption("jah?")
gameplay= True

#kujund
a=20
b=20
#kiirus
v= 5

#mängu loop
while gameplay:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type== pg.QUIT:
            gameplay=False
    keys=pg.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x-= v
    if keys[pygame.K_RIGHT] and x<300-a:
        x+= v
    if y<500:
        y+=5
    else:
        y=50
        xk=randint(0,280)

    #joonistame
    aken.fill((200,200,200))
    #tegelintski
    pg.draw.rect(aken, (100,150,150), (x, 480, a, b))

    pg.draw.rect(aken,(0, 255, 255), (xk, y, a, b))
    pg.display.update()





pygame.quit()

