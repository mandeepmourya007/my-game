import pygame
import random
pygame.init()
width=360
height=360
screen_size=(width,height)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("flappy cube")
#color
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
#color list
color=[black,red,green,blue]
poll_x=width-10
clock=pygame.time.Clock()
change_x=h=0
n=2 #normal coliu7r i.e default
d=1 #whel poll near co.loe red
rc=n
i=width+3
i2=i+random.randint(width+10,width+50)
i3=i2+random.randint(width+10,width+50)
pw=100 #pool width
while("playing"):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
               #logic for jump
                h-=20
             #   x+=1
            if event.key==pygame.K_q:
                pygame.quit()
                quit()
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
    screen.fill(white)
##    poll_x-=0
##    if poll_x==0:
##        poll_x=width
    h+=1
    pygame.draw.rect(screen,color[n],(height/2,width/2+h,10,10)) #box

   # for i in range(0,1000,155):
    
    pygame.draw.rect(screen,color[rc],(i,0,pw,150))        #upper plol
    pygame.draw.rect(screen,color[rc],(i,190,pw,170))  #lower poll
        
    pygame.draw.rect(screen,color[rc],(i2,0,pw,150))        #upper plol
    pygame.draw.rect(screen,color[rc],(i2,190,pw,170))  #lower pollpygame.draw.rect(screen,color[rc],(poll_x+i,0,10,150))        #upper plol

    pygame.draw.rect(screen,color[rc],(i3,0,pw,150))  #lower pollpygame.draw.rect(screen,color[rc],(poll_x+i,0,10,150))        #upper plol
    pygame.draw.rect(screen,color[rc],(i3,190,pw,170))  #lower poll
    if (height/2<=i and i<=height/2+pw) or (height/2<=i2 and i2<=height/2+pw) or(height/2<=i3 and i3<=height/2+pw) :
        rc=d
    else:
        rc=n
    i-=5
    i2-=5
    i3-=5

    pygame.display.update()
    clock.tick(30)            
            
                


