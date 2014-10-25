__author__ = 'samirpatil'
import pygame, sys
from pygame.locals import *

pygame.init()
LEFT = 1

#set up the window
DISPLAYSURF = pygame.display.set_mode((300,300))
pygame.display.set_caption('Drawing')

#set up the colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
#draw on the surface object
DISPLAYSURF.fill(WHITE)

"""rect objects for division of screen in parts so that we can use collidepoint function of rect objects to check if
the point we clicked lies in the square or not"""
s1 = pygame.Rect(0, 0, 100, 100)
s2 = pygame.Rect(100, 0, 100, 100)
s3 = pygame.Rect(200, 0, 100, 100)
s4 = pygame.Rect(0, 100, 100, 100)
s5 = pygame.Rect(100, 100, 100, 100)
s6 = pygame.Rect(200, 100, 100, 100)
s7 = pygame.Rect(0, 200, 100, 100)
s8 = pygame.Rect(100, 200, 100, 100)
s9 = pygame.Rect(200, 200, 100, 100)
# array of rect objects for effective looping
check=[s1, s2, s3, s4, s5, s6, s7, s8, s9]
# surface objects respective to rect objects for filling purpose
b1=pygame.Surface((100, 100))
b2=pygame.Surface((100, 100))
b3=pygame.Surface((100, 100))
b4=pygame.Surface((100, 100))
b5=pygame.Surface((100, 100))
b6=pygame.Surface((100, 100))
b7=pygame.Surface((100, 100))
b8=pygame.Surface((100, 100))
b9=pygame.Surface((100, 100))
# again array for effective looping
n=3
j=0
# j will have the value of pre coloured square number
# n is matrix suffix of squares (eg 3x3 here)
fill=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
for d in range (0,9):
    fill[d].fill(RED)
def dline():




    pygame.draw.line(DISPLAYSURF,GREEN,(0, 0),(0,300),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(0,0),(300,0),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(300,300),(300,0),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(300,300),(0,300),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(0,100),(300,100),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(0,200),(300,200),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(100,0),(100,300),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(200,0),(200,300),1)

def filler(prev, curr):
    #these conditions check whether the current point is up,down,left,right of the previous point and then only fills it
    #and returns 1

    if curr==(prev-n):

        fill[curr].fill(BLUE)
        return 1

    elif curr==(prev-1) and\
         (prev-1) != (n-1) and\
         (prev-1) != (2*n-1):

        fill[curr].fill(BLUE)
        return 1

    elif curr==(prev+1) and\
         (prev+1) != (n) and\
         (prev+1) != (2*n):

        fill[curr].fill(BLUE)
        return 1

    elif curr==(prev+n):


        fill[curr].fill(BLUE)
        return 1
    else:
        return 0



















# variables for storing coordinates of point clicked
x = 0
y = 0
# creating a static level
fill[0].fill(BLUE)
fill[8].fill(BLUE)


# run the game loop
while True:
    DISPLAYSURF.blit(b1,(0,0))
    DISPLAYSURF.blit(b2,(100,0))
    DISPLAYSURF.blit(b3,(200,0))
    DISPLAYSURF.blit(b4,(0,100))
    DISPLAYSURF.blit(b5,(100,100))
    DISPLAYSURF.blit(b6,(200,100))
    DISPLAYSURF.blit(b7,(0,200))
    DISPLAYSURF.blit(b8,(100,200))
    DISPLAYSURF.blit(b9,(200,200))
    dline()






    for event in pygame.event.get():
        if event.type==QUIT:
             pygame.quit()
             sys.exit()

        for i in range(0,9):

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x, y = event.pos
                color = pygame.PixelArray(DISPLAYSURF)


                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLUE):
                    print(i)
                    h= filler(j, i)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h==1:
                        j=i
                    else:
                        #for debugging purpose
                        print("wrong selection")


                #we have to delete the pixel array object after use otherwise it will give error like
                #surface is blocked
                del color









    pygame.display.update()


