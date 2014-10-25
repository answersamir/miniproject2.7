__author__ = 'Rashi'

import pygame, sys, math
from pygame.locals import *

pygame.init()
# mouse button
LEFT = 1
# 5*5 matrix
n = 5
red = 0
green = 0
yellow = 0
blue = 0
purple = 0

# respective colour's previous tiles (which user will give as precoloured tiles by clicking on it)



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
fill(colour)
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
# flags for checking which colours to fill
flagred = False
flagblue = False
flagyellow = False
flaggreen = False
flagpurple = False
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



        for i in range(0,n*n):

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x, y = event.pos
                color = pygame.PixelArray(DISPLAYSURF)
                # for RED tiles
                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(RED) and (i == 0 or i == 21):
                    red=i
                    print(i)
                    print(red)
                    flagred = True
                    flaggreen = False
                    flagyellow = False
                    flagblue = False
                    flagpurple = False
                # only if a red tile is checked then user will be able to colour further tiles as red
                #same applies to next cases for different colours
                elif flagred==True:
                    if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                        print(check[i])
                        print(i)
                        print(red)


                        h= filler(red, i, RED)
                        #if h is one filling has ocurred then we can change the previous point to current point
                        if h==1:
                            red=i
                            print(red)

                        else:
                            #for debugging purpose
                            print("wrong selection")


                # for Green tiles
                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(GREEN) and (i == 16 or i == 2):
                    green=i
                    print(i)
                    print(green)
                    flaggreen = True
                    flagred = False
                    flagyellow = False
                    flagblue = False
                    flagpurple = False

                elif flaggreen==True:
                    if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                        print(check[i])
                        print(i)
                        print(green)


                        h = filler(green, i, GREEN)
                        #if h is one filling has ocurred then we can change the previous point to current point
                        if h == 1:
                            green=i
                            print(green)

                        else:
                            #for debugging purpose
                            print("wrong selection")

                # for Yellow tiles
                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(YELLOW) and (i == 18 or i == 4):
                    yellow=i
                    print(i)
                    print(yellow)
                    flaggreen = False
                    flagred = False
                    flagyellow = True
                    flagblue = False
                    flagpurple = False

                elif flagyellow == True:
                    if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                        print(check[i])
                        print(i)
                        print(yellow)



                        h= filler(yellow, i, YELLOW)
                        #if h is one filling has ocurred then we can change the previous point to current point
                        if h==1:
                            yellow=i
                            print(yellow)

                        else:
                            #for debugging purpose
                            print("wrong selection")


                # for BLUE tiles
                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLUE) and (i == 7 or i == 22):
                    blue = i
                    print(i)
                    print(blue)
                    flaggreen = False
                    flagred = False
                    flagyellow = False
                    flagblue = True
                    flagpurple = False

                elif flagblue == True:
                    if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                        print(check[i])
                        print(i)
                        print(blue)


                        h= filler(blue, i, BLUE)
                        #if h is one filling has ocurred then we can change the previous point to current point
                        if h == 1:
                            blue = i
                            print(blue)

                        else:
                            #for debugging purpose
                            print("wrong selection")

                # for Purple tiles
                if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(PURPLE) and (i == 9 or i == 23):
                    purple = i
                    print(i)
                    print(purple)
                    flaggreen = False
                    flagred = False
                    flagyellow = False
                    flagblue = False
                    flagpurple = True

                elif flagpurple == True:
                    if check[i].collidepoint(x, y) and color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                        print(check[i])
                        print(i)
                        print(purple)


                        h= filler(purple, i, PURPLE)
                        #if h is one filling has ocurred then we can change the previous point to current point
                        if h == 1:
                            purple = i
                            print(purple)

                        else:
                            #for debugging purpose
                            print("wrong selection")







                #we have to delete the pixel array object after use otherwise it will give error like
                #surface is blocked
                del color
    pygame.display.update()


__author__ = 'samirpatil'
