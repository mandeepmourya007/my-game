import pygame
import random
pygame.init()
width=480
height=360
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("skatter BOy")

#images

road=pygame.image.load("roada.jpg")
rwh=road.get_size()
clock=pygame.time.Clock()

#color
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(237,218,15)
ORANGE =(237,118,15)

x1=0
x2=0
x3=0
sx=470
sy=int(rwh[0]/2)
cx=30
cy=int(rwh[1]/2)
cx_c=0
cy_c=0
s=0
ry=random.randrange(rwh[1])
def msg(text,color,x,y,size=25):
    font=pygame.font.SysFont(None,size)
    msg=font.render(text,True,color,)
    screen.blit(msg,(x,y))
    
def explosion(e_x,e_y):
    mag=1
    clock.tick(10)
    color=[RED,YELLOW,ORANGE]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                quit()
        e_x=e_x+random.randrange(-1*mag,mag)
        e_y=e_y+random.randrange(-1*mag,mag)
        mag+=1
        if mag==30:
            break
        pygame.draw.circle(screen,color[random.randrange(0,3)],(e_x,e_y),5)
        
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
                cy_c-=3
            if event.key==pygame.K_DOWN:
                cy_c+=3
            if event.key==pygame.K_RIGHT:
                cx_c+=3
            if event.key==pygame.K_LEFT:
                cx_c-=3    
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                cy_c=0
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
           
                cx_c=0
    cx+=cx_c
    cy+=cy_c
            
    if x1+rwh[0]<0:
        x1=width
    if x2+2*rwh[0]<0:
        x2=width-rwh[0]

    if x3+3*rwh[0]<0:
        x3=width-2*rwh[0]
   
    
    if sx+30<0:
        sx=width
        ry=random.randrange(rwh[1]-30)

    sx-=10
    x1-=10
    x3-=10
    x2-=10
    screen.fill(WHITE)
    screen.blit(road,(x1,5))
    screen.blit(road,(x2+rwh[0],5))
    screen.blit(road,(x3+2*rwh[0],5))
    stone=pygame.draw.rect(screen,BLACK,(sx,ry,30,30))
    car =pygame.draw.circle(screen,WHITE,(40+cx,cy,),18)
    if stone.colliderect(car):
        sx=width
        ry=random.randrange(rwh[1]-30)
        explosion(40+cx,cy)
        s+=1
        
    msg("score:"+str(s),BLACK,50,190)   

    pygame.display.update()
    clock.tick(20)
