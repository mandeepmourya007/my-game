import pygame
import time
import random
pygame.init()
width=420
height=420
piece=10
size_of_screen=(width,height)
screen=pygame.display.set_mode(size_of_screen)
pygame.display.set_caption("SNAKE GAME               BY MANDEEP")
WHITE= (255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,215)
ORANGE =(237,118,15)
YELLOW=(237,218,15)
COLOR=[WHITE,RED,BLACK,GREEN,BLUE,ORANGE,YELLOW]
FPS=pygame.time.Clock()
i=0 #to speed up game
#snake
def snake(snake_list,color,piece):
    global body
##    snake_lenght=0
    for xny in snake_list:
       # if len(snake_list)==snake_lenght:
        body=pygame.draw.rect(screen,color,(xny[0],xny[1],piece,piece))

#message
font=pygame.font.SysFont(None,size=30)
def message(text,color,xm,ym,size=30):
    global font
    screen_text=font.render(text,True,color)
    screen.blit(screen_text,(xm,ym))
#game intro
def game_intro():
    intro=True
    while intro:

        screen.fill(BLACK)
        message("game by MANDEEP",GREEN,150,150)
        message("Wellcome to snake game",WHITE,50,10)
        message("Press ENTER to PLAY game ",ORANGE,50,50,20)
        message("Press ESCAPE to quit",RED,50,90,20)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    snake_game()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            
            pygame.display.update()
                
     
    
    
    

#eating think
def generate_eat():
    global eat_x,eat_y
    eat_x=round(random.randint(15,width-piece-15)/10)*10
    eat_y=round(random.randint(15,height-piece-15)/10)*10
generate_eat()

def snake_game():
    gameover=False
    x=100
    y=100
    x_change=0
    y_change=0
    snake_list=[]
    snake_lenght=1
    i=0
    generate_eat()
    while not gameover:
        for event in pygame.event.get():
           
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-piece-2
                    y_change=0
                elif event.key==pygame.K_RIGHT:
                    x_change=piece+2
                    y_change=0
                elif event.key==pygame.K_UP:
                    y_change=-piece-2
                    x_change=0
                   
                elif event.key==pygame.K_DOWN:
                    y_change=piece+2
                    x_change=0
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        x+=x_change
        y+=y_change

        if x<=10 or x>=width-10:
            gameover=True

        if y<=10 or y>=height-10:
            gameover=True
        #body.colliderect(eat)
        #body is not defined
            #think why
        if (x<=eat_x+piece and x+piece>=eat_x) and (y+piece>=eat_y and y<=eat_y+piece):
                generate_eat()
                snake_lenght=snake_lenght+1
                    
        if snake_lenght==10:
            i=3
        if snake_lenght==20:
            i=6
        if snake_lenght==30:
            i=9
        if snake_lenght==40:
            i=12
            
        snake_head=[[x,y]]
        snake_list=snake_list+snake_head
        if snake_lenght <len(snake_list):
            del snake_list[0]
        
        screen.fill(WHITE)
        rc=random.randint(0,6)
        message("game by MANDEEP",COLOR[rc],220,10)
        message("score: "+str(snake_lenght-1),BLACK,10,10)
        bu= pygame.draw.rect(screen,BLUE,(0,0,width,10))
        bl=pygame.draw.rect(screen,BLUE,(0,0,10,height))
        br= pygame.draw.rect(screen,BLUE,(width-10,0,10,height))
        bd= pygame.draw.rect(screen,BLUE,(0,height-10,width,10))
        snake(snake_list,GREEN,piece)   
        eat=pygame.draw.circle(screen,COLOR[rc],(int(eat_x),int(eat_y)),piece-3)


# I can also use collide as below insted of   using x y
##        if body.colliderect(br):#x==10 or x>=width-10:
##            gameover=True
##         

        FPS.tick(12+i)        
        pygame.display.update()
        
    message("Game over",RED,100,100)
    message("your score is "+str(snake_lenght-1),BLACK,100,151)
    pygame.display.update()
    time.sleep(2)
    game_intro()
game_intro()

