
__author__ = 'samirpatil'
import pygame, sys
import numpy as np
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
n=3
j=0


check = [[[pygame.Rect(countx*100, county*100, 100, 100)] for countx in range(n)] for county in range(n)]

"""rect objects for division of screen in parts so that we can use collidepoint function of rect objects to check if
the point we clicked lies in the square or not"""

# surface objects respective to rect objects for filling purpose
fill = [[[pygame.Surface((100, 100))] for countx in range(n)] for county in range(n)]
print(fill[0][0])


# again array for effective looping

count2 = 0
count1 = 0
# j will have the value of pre coloured square number
# n is matrix suffix of squares (eg 3x3 here)

for county in range(0,n):
    for countx in range(0,n):
        r=0


def reccheckleft(place, k):
   if k == n*n:
        return 1
   if place != (k-1):
        reccheckleft(place, k+n)
   else:return 0


def reccheckright(place, k):
    if k == n*n:

        return 1

    if place !=(k):
        reccheckright(place, k+n)
    else:
        return 0



def dline():
    pygame.draw.line(DISPLAYSURF,GREEN,(0, 0),(0,300),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(0,0),(300,0),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(300,300),(300,0),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(300,300),(0,300),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(0,100),(300,100),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(0,200),(300,200),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(100,0),(100,300),1)
    pygame.draw.line(DISPLAYSURF,GREEN,(200,0),(200,300),1)

"""def filler(prev, curr):
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
        return 0"""

# variables for storing coordinates of point clicked
x = 0
y = 0
# creating a static level
fill[0][0].fill(BLUE)
fill[8].fill(BLUE)


# run the game loop
while True:
    for county in range(0,n):
        for countx in range(0,n):
            DISPLAYSURF.blit(fill[county][countx],(countx*100,county*100))

    dline()






    """for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        for i in range(0,n*n):


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x, y = event.pos
                color = pygame.PixelArray(DISPLAYSURF)



                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(RED):
                    print(check[i])

                    h=filler(j, i)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h ==1 :
                        j = i
                    else:
                        #for debugging purpose
                        print("wrong selection")


                #we have to delete the pixel array object after use otherwise it will give error like
                #surface is blocked
                del color"""









    pygame.display.update()


