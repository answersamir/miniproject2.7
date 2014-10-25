__author__ = 'samirpatil'

import pygame, sys
from pygame.locals import *

pygame.init()
LEFT = 1
n = 5
j = 0
k = 2
l = 4
m = 7
o = 9

# j will have the value of pre coloured square number
# n is matrix suffix of squares (eg 5x5 here)


#set up the window
DISPLAYSURF = pygame.display.set_mode((n*100, n*100))
pygame.display.set_caption('BRIDGES')

#set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
#draw on the surface object
DISPLAYSURF.fill(WHITE)


"""rect objects for division of screen in parts so that we can use collidepoint function of rect objects to check if
the point we clicked lies in the square or not"""

check = []
for county in range(0,n):
    for countx in range(0,n):
        check.append(pygame.Rect(countx*100, county*100, 100, 100))

# surface objects respective to rect objects for filling purpose

fill = []
for county in range(0,n):
    for countx in range(0,n):
        fill.append(pygame.Surface((100, 100)))




# again array for effective looping

# default colour if kept white the loop is not working
for d in range(0, n*n):
    fill[d].fill(BLACK)
def dline():
    for count in range(0, n):
        # horizontal lines
        pygame.draw.line(DISPLAYSURF, WHITE, (0, count*100), (n*100, count*100), 1)
        # vertical lines
        pygame.draw.line(DISPLAYSURF, WHITE, (count*100, 0), (count*100, n*100), 1)


def filler(prev, curr, colour):
    #these conditions check whether the current point is up,down,left,right of the previous point and then only fills it
    #and returns 1

    if curr == (prev-n):

        fill[curr].fill(colour)
        return 1

    elif curr == (prev-1) and\
         (prev-1) != (n-1) and\
         (prev-1) != (2*n-1)and\
         (prev-1) != (3*n-1)and\
         (prev-1) != (4*n-1):

        fill[curr].fill(colour)
        return 1

    elif curr == (prev+1) and\
         (prev+1) != (n) and\
         (prev+1) != (2*n)and\
         (prev+1) != (3*n)and\
         (prev+1) != (4*n):

        fill[curr].fill(colour)
        return 1

    elif curr == (prev+n):

        fill[curr].fill(colour)
        return 1
    else:
        return 0
# variables for storing coordinates of point clicked
x = 0
y = 0
# creation of a static level
fill[0].fill(RED)
fill[21].fill(RED)
fill[16].fill(GREEN)
fill[2].fill(GREEN)
fill[7].fill(BLUE)
fill[22].fill(BLUE)
fill[4].fill(YELLOW)
fill[18].fill(YELLOW)
fill[23].fill(PURPLE)
fill[9].fill(PURPLE)


# run the game loop
while True:
    for county in range(0,n):
        for countx in range(0,n):
              DISPLAYSURF.blit(fill[n*county+countx],(countx*100,county*100))
    dline()





    for event in pygame.event.get():
        if event.type==QUIT:
             pygame.quit()
             sys.exit()



        for i in range (0,n*n):

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x, y = event.pos
                color = pygame.PixelArray(DISPLAYSURF)


                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                    print(check[i])
                    print(i)
                    print(j)


                    h= filler(j, i, RED)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h==1:
                        j=i
                        print(j)

                    else:
                        #for debugging purpose
                        print("wrong selection")

                    h = filler(k, i, GREEN)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h==1:
                        k=i
                        print(k)
                    else:
                        #for debugging purpose
                        print("wrong selection")

                    h= filler(l, i, YELLOW)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h==1:
                        l=i
                        print(l)
                    else:
                        #for debugging purpose
                        print("wrong selection")

                    h= filler(m, i, BLUE)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h==1:
                        m=i
                        print(m)
                    else:
                        #for debugging purpose
                        print("wrong selection")

                    h= filler(o, i, PURPLE)
                    #if h is one filling has ocurred then we can change the previous point to current point
                    if h==1:
                        o=i
                        print(o)
                    else:
                        #for debugging purpose
                        print("wrong selection")





                #we have to delete the pixel array object after use otherwise it will give error like
                #surface is blocked
                del color
    pygame.display.update()


