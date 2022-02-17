#all imports
import pygame
import time
import sys
import random

#init
pygame.init()

#CONST vars
WIDTH=600
HEIGHT=400
GRAVITY= 9.8;
pipes=[]

class Bird:
    def __init__(self,x,y,lives,speed,jumpspeed,framespeed):
        self.imgs= [pygame.image.load("res/img/bird/1.png"),pygame.image.load("res/img/bird/2.png"),pygame.image.load("res/img/bird/3.png"),pygame.image.load("res/img/bird/2.png")]
        self.currentImgIndex=0
        self.currentImg=self.imgs[self.currentImgIndex]
        self.x=x
        self.y=y
        self.width=self.currentImg.get_width()
        self.height=self.currentImg.get_height()
        self.lives=lives
        self.speed=speed
        self.velocity=0
        self.jumpspeed= jumpspeed
        self.frame_speed= framespeed
        self.passed_time=0
    
    def move(self,deltatime):
        if self.y > HEIGHT-self.height:
            self.y=HEIGHT-self.height
        elif self.y < 0:
            self.y=0
            self.velocity=0
        else:
            newy= (self.velocity * deltatime) + (self.speed * GRAVITY * deltatime * deltatime)
            if deltatime !=0:
                self.velocity= newy/deltatime
            self.y= self.y+newy
    
        
        
    def draw(self,screen,deltatime):
        self.passed_time+= deltatime
        if self.passed_time > self.frame_speed:
            #change currentImg
            self.currentImgIndex+=1
            if self.currentImgIndex >= len(self.imgs):
                self.currentImgIndex=0
            self.currentImg= self.imgs[self.currentImgIndex]
            self.passed_time=0

        self.width=self.currentImg.get_width()
        self.height=self.currentImg.get_height()
        screen.blit(self.currentImg,(self.x,self.y))
        
    def jump(self):
        self.velocity=self.jumpspeed
      
      
def SpawnPipe(speed,height,width,x):
    direction= random.randint(1,2)
    up=False
    if direction==1:
        up=True
    y=0
    if up:
        y= random.randint(HEIGHT-height+10,HEIGHT-40)
    else:
        y= random.randint(-(height)+40,-10)
    pipes.append(Pipe(x,y,up,speed))


class Pipe:
    def __init__(self,x,y,up,speed):
        self.speed=speed
        self.x=x
        self.y=y
        self.up=up
        self.img= pygame.image.load("res/img/pipe.png")
        self.width=self.img.get_width()
        self.height=self.img.get_height()
        scale_factor=1.5
        self.img= pygame.transform.scale(self.img,(self.width/scale_factor,self.height/scale_factor))
        self.width/=scale_factor
        self.height/=scale_factor
        if not self.up:
            #rotate img
            self.img= pygame.transform.rotate(self.img,180)
    
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
            
    
    def move(self,deltatime):
        self.x-= self.speed * deltatime
        if self.x <0:
            #delete this pipe and add another one
            pipes.remove(self)
            SpawnPipe(self.speed,self.height,self.width,WIDTH-self.width+self.x)


def update(screen,deltatime,bird,pipes,background):
    #moving everything
        
    bird.move(deltatime)
    for pipe in pipes:
        pipe.move(deltatime)
    
    #drawing everything
    screen.fill((0,0,0))
    background_width= background.get_width()
    for i in range(0,WIDTH,background_width):
        screen.blit(background,(i,0))
    bird.draw(screen,deltatime)
    for pipe in pipes:
        pipe.draw(screen)
    pygame.display.flip()
        

def main():
    screen= pygame.display.set_mode((WIDTH,HEIGHT))
    game_over=False
    x=50
    y=20
    speed=80
    jumpspeed=-300
    frame_speed= 0.2
    bird= Bird(x,y,1,speed,jumpspeed,frame_speed)
    pipes_speed=150
    pipe_template= Pipe(0,0,True,pipes_speed)
    
    temp_x=WIDTH-pipe_template.width
    for i in range(4):
        SpawnPipe(pipes_speed,pipe_template.height,pipe_template.width,temp_x)
        temp_x+=150
    
    background= pygame.image.load("res/img/background.png")
    start= time.time()
    while(not game_over):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type== pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    bird.jump()
        now= time.time()
        deltatime= now-start
        start=now
        update(screen,deltatime,bird,pipes,background)
        

#core of program    
if __name__=="__main__":
    main()
else:
    print("This is not a module, please run it directly")