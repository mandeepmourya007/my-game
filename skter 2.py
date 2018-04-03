import pygame
import random
pygame.init()
w=360
h=150
size=(w,h)
screen=pygame.display.set_mode(size)
BLACK=(0,0,0)
STONE=(188, 158, 26)
BLUE=(0,0,255)
WHITE=(255,255,255)
SAND=(229, 214, 149)
x=0
y=111
yc=0
xc=0
def jump():
    global yc,y
    if yc==1:
        y-=yc
        if y==80:
           
            yc=0
    if yc==0:
        if 80<=y<=111:
        
      
            y+=1
    if y==111:
       y=111
def stone():
    global sx,sy
    sx=[]
    sy=[]
    for i in range(30):
        sx=sx+[random.randrange(1,350,30)]
    for i in range(30):
        sy=sy+[random.randrange(136,150,5)]
clock=pygame.time.Clock()
    
stone()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key==pygame.K_UP:
                yc=1
            if event.key==pygame.K_LEFT:
                xc=-1
            if event.key==pygame.K_RIGHT:
                xc=1
            
    jump()
    x+=xc
    screen.fill(WHITE)
    char=pygame.draw.rect(screen,BLUE,(20+x,y,20,20))
    pygame.draw.rect(screen,SAND,(1,131,360,19))
    for i in range(30):
        pygame.draw.rect(screen,BLACK,(sx[0],116,15,15))
        pygame.draw.circle(screen,STONE,(sx[i],sy[i],),5)
        sx[i]-=5
        if sx[i]<0:
            sx[i]=350
        pygame.display.update()
    pygame.display.update()
    clock.tick(30)  
