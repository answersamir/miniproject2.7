__author__ = 'samirpatil'
# Current condition : No success yet
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
arr_red = []
arr_blue = []
arr_green = []
arr_yellow = []
arr_purple = []
bluecount = 0
redcount = 0
greencount = 0
yellowcount = 0
purplecount = 0

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
# flags for checking which colours to fill
flagred = False
flagblue = False
flagyellow = False
flaggreen = False
flagpurple = False
xfault = 0
yfault = 0
isDragging = 0
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


        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            color = pygame.PixelArray(DISPLAYSURF)
            if color[x, y] == DISPLAYSURF.map_rgb(RED):
                isDragging = 1
                choose = RED

                xfault = x
                yfault = y

            elif color[x, y] == DISPLAYSURF.map_rgb(GREEN):
                isDragging = 1
                choose = GREEN
                xfault = x
                yfault = y

            elif color[x, y] == DISPLAYSURF.map_rgb(YELLOW):
                isDragging = 1
                choose = YELLOW
                xfault = x
                yfault = y

            elif color[x, y] == DISPLAYSURF.map_rgb(BLUE):
                isDragging = 1
                choose = BLUE
                xfault = x
                yfault = y

            elif color[x, y] == DISPLAYSURF.map_rgb(PURPLE):
                isDragging = 1
                choose = PURPLE
                xfault = x
                yfault = y

        # dragging starts from this point no need to colour it
            del color

        if event.type == pygame.MOUSEBUTTONUP:
            isDragging = 0

            print("mouse button is up")



        if event.type == pygame.MOUSEMOTION and isDragging == 1:
            print(isDragging)
            color = pygame.PixelArray(DISPLAYSURF)
            x, y = event.pos
            if color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                for i in range(0, n*n):
                    if check[i].collidepoint(x, y):
                        fill[i].fill(choose)


            elif color[x, y] == DISPLAYSURF.map_rgb(BLUE):
                choose = BLUE

            elif color[x, y] == DISPLAYSURF.map_rgb(RED):
                choose = RED
            elif color[x, y] == DISPLAYSURF.map_rgb(PURPLE):
                choose = PURPLE
            elif color[x, y] == DISPLAYSURF.map_rgb(YELLOW):
                choose = YELLOW
            elif color[x, y] == DISPLAYSURF.map_rgb(GREEN):
                choose = GREEN
                #pygame.mouse.set_pos(xfault, yfault)
            print(x, y)

            del color
       #we have to delete the pixel array object after use otherwise it will give error like
                #surface is blocked









    pygame.display.update()


