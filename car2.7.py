
import pygame
import random
try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
pygame.init()
width=480
height=360
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("skatter BOy")

#images

road=pygame.image.load("road.jpg")
rwh=road.get_size()
clock=pygame.time.Clock()

#color
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(237,218,15)
ORANGE =(237,118,15)

y1=0
y2=0
y3=0
sx=random.randrange(50,rwh[0])
sy=int(rwh[0]/2)
cx=int(rwh[0]/2)
cy=300
cx_c=0
cy_c=0
s=0
ry=0
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
    if cx>rwh[0]+50:
        cx=rwh[0]+50
    if cx<50:
        cx=50
    cx+=cx_c
    cy+=cy_c
            
    if y1+rwh[1]<0:
        y1=height
    if y2+2*rwh[1]<0:
        y2=height-rwh[1]

    if y3+3*rwh[1]<0:
        y3=height-2*rwh[1]
   
    
    if ry+30>480:
        sx=random.randrange(50,rwh[0])
        ry=0

    ry+=10
    y1-=10
    y3-=10
    y2-=10
    screen.fill(WHITE)
    screen.blit(road,(50,y1))
    screen.blit(road,(50,y2+rwh[1]))
    screen.blit(road,(50,y3+2*rwh[1]))
    stone=pygame.draw.rect(screen,BLACK,(sx,ry,30,30))
    car =pygame.draw.circle(screen,WHITE,(cx,cy,),18)
    if stone.colliderect(car):
        sx=random.randrange(rwh[0]-30)
        ry=height
        explosion(40+cx,cy)
        s+=1    
    msg("score:"+str(s),BLACK,250,20)   

    pygame.display.update()
    clock.tick(20)
