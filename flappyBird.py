#all imports
import pygame
import time
import sys

#init
pygame.init()

#CONST vars
WIDTH=600
HEIGHT=400


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
    speed=100
    start= time.time()
    while(not game_over):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
        now= time.time()
        deltatime= now-start
        start=now
        x,y= update(deltatime,x,y,speed)
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(x,y,width,height))
        pygame.display.flip()
        


#core of program    
if __name__=="__main__":
    main()
else:
    print("This is not a module, please run it directly")