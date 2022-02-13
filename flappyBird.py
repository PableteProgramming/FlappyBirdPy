#all imports
import pygame
import time
import sys

#init
pygame.init()

#CONST vars
WIDTH=600
HEIGHT=400
GRAVITY= 9.8;

class Bird:
    def __init__(self,x,y,width,height,lives,speed):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.lives=lives
        self.speed=speed
        self.velocity=0
    
    def move(self,deltatime):
        newy= (self.velocity * deltatime) + (self.speed * GRAVITY * deltatime * deltatime)
        if deltatime !=0:
            self.velocity= newy/deltatime
        self.y= self.y+newy
        
    def draw(self,screen):
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.x,self.y,self.width,self.height))
        pygame.display.flip()
        
    def update(self,deltatime,screen):
        self.move(deltatime)
        self.draw(screen)
        

#functions
def update(deltatime,x,y,speed):
    nx= x+(speed*deltatime)
    ny= y+(speed*deltatime)
    return (nx,ny)

def main():
    screen= pygame.display.set_mode((WIDTH,HEIGHT))
    game_over=False
    x=0
    y=0
    width=20
    height=20
    speed=80
    bird= Bird(x,y,width,height,1,speed)
    start= time.time()
    while(not game_over):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
        now= time.time()
        deltatime= now-start
        start=now
        bird.update(deltatime,screen)
        
        


#core of program    
if __name__=="__main__":
    main()
else:
    print("This is not a module, please run it directly")