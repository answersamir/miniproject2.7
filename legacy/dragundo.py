__author__ = 'samirpatil'

import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

FRAMES = 30
# mouse button
LEFT = 1
# nxn matrix
n = 7
#arrays and counts for all the used colours (used to undo the last step)
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

#set up the window
DISPLAYSURF = pygame.display.set_mode((n*75, n*75+75))
DISPLAYSURF.convert_alpha()
pygame.display.set_caption('BRIDGES')

#set up the colors
BLACK = (96, 96, 96)
WHITE = (255, 255, 255)
RED = (255, 90, 90)
GREEN = (90, 255, 90)
BLUE = (90, 90, 255)
PURPLE = (128, 90, 128)
YELLOW = (255, 255, 90)
ORANGE = (255, 165, 0)
GOLD = (218, 165, 32)
TURQ = (64, 224, 208)
LIGHTY = (255, 255, 224)
#draw on the surface object
DISPLAYSURF.fill(LIGHTY)


"""rect objects for division of screen in parts so that we can use collidepoint function of rect objects to check if
the point we clicked lies in the square or not"""

check = []
for county in range(0, n):
    for countx in range(0, n):
        check.append(pygame.Rect(countx*75, county*75, 75, 75))

# surface objects respective to rect objects for filling purpose

fill = []
for county in range(0, n):
    for countx in range(0, n):
        fill.append(pygame.Surface((75, 75)))




for d in range(0, n*n):
    fill[d].fill(BLACK)

#implemented class for code readability
class button:
    def __init__(self, name):
        self.text = name
        self.xtop = 0
        self.ytop = 0
        self.width = 0
        self.height = 0
        self.rect = 0


    def button_coordinates(self, a, b, width, height):
        self.xtop = a
        self.ytop = b
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.xtop, self.ytop, self.height, self.width)

    def place_button(self, image):


        DISPLAYSURF.blit(image, (self.xtop, self.ytop))

        #currently just filling the surf will blit image afterwards




def dline():
    for count in range(0, n):
        # horizontal lines
        pygame.draw.line(DISPLAYSURF, WHITE, (0, count*75), (n*75, count*75), 1)
        # vertical lines
        pygame.draw.line(DISPLAYSURF, WHITE, (count*75, 0), (count*75, n*75), 1)




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

#variable for identification of dragging event
isDragging = 0

b1 = button("UNDO")
b1.button_coordinates(0, n*75, 75, 75)
b1.place_button(pygame.image.load('undo1.png'))

b2 = button("RESTART")
b2.button_coordinates(75, n*75, 75, 75)
b2.place_button(pygame.image.load('restart.png'))




# run the game loop
while True:
    clock.tick(FRAMES)


    for county in range(0, n):
        for countx in range(0, n):
              DISPLAYSURF.blit(fill[n*county+countx], (countx*75, county*75))



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
                del color



            elif color[x, y] == DISPLAYSURF.map_rgb(GREEN):
                isDragging = 1
                choose = GREEN
                del color


            elif color[x, y] == DISPLAYSURF.map_rgb(YELLOW):
                isDragging = 1
                choose = YELLOW
                del color


            elif color[x, y] == DISPLAYSURF.map_rgb(BLUE):
                isDragging = 1
                choose = BLUE
                del color

            elif color[x, y] == DISPLAYSURF.map_rgb(PURPLE):
                isDragging = 1
                choose = PURPLE
                del color


            elif b1.rect.collidepoint(x, y):
                del color
                print "undo button pressed"
                b1.place_button(pygame.image.load('undo_click.png'))

            elif b2.rect.collidepoint(x, y):
                del color
                print "undo button pressed"
                b2.place_button(pygame.image.load('restart_click.png'))

            else:
                del color



        # dragging starts from this point no need to colour it


        if event.type == pygame.MOUSEBUTTONUP:
            isDragging = 0
            x, y = event.pos
            color = pygame.PixelArray(DISPLAYSURF)
            if b1.rect.collidepoint(x, y):
                print "i am in"
                del color
                while bluecount > 0:
                    fill[arr_blue[bluecount-1]].fill(BLACK)
                    bluecount -= 1
                while redcount > 0:
                    fill[arr_red[redcount-1]].fill(BLACK)
                    redcount -= 1
                while purplecount > 0:
                    fill[arr_purple[purplecount-1]].fill(BLACK)
                    purplecount -= 1
                while greencount > 0:
                    fill[arr_green[greencount-1]].fill(BLACK)
                    greencount -= 1
                while yellowcount > 0:
                    fill[arr_yellow[yellowcount-1]].fill(BLACK)
                    yellowcount -= 1
                del arr_blue[:]
                del arr_purple[:]
                del arr_green[:]
                del arr_yellow[:]
                del arr_red[:]

                b1.place_button(pygame.image.load('clear.png'))
                b1.place_button(pygame.image.load('undo1.png'))

            elif b2.rect.collidepoint(x, y):
                del color
                for d in range(0, n*n):
                    fill[d].fill(BLACK)
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
                b2.place_button(pygame.image.load('clear.png'))
                b2.place_button(pygame.image.load('restart.png'))


            else:
                del color
            print("mouse button is up")



        if event.type == pygame.MOUSEMOTION and isDragging == 1:
            print(isDragging)
            color = pygame.PixelArray(DISPLAYSURF)
            x, y = event.pos
            if color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                for i in range(0, n*n):
                    if check[i].collidepoint(x, y):
                        fill[i].fill(choose)
                        # now we keep a list of latest filled square to undo them, we also delete the last coloured entries
                        if choose == RED:
                            del arr_blue[:]
                            del arr_purple[:]
                            del arr_green[:]
                            del arr_yellow[:]
                            bluecount = 0
                            purplecount = 0
                            greencount = 0
                            yellowcount = 0
                            arr_red.append(i)
                            redcount += 1
                        elif choose == BLUE:
                            del arr_red[:]
                            del arr_purple[:]
                            del arr_green[:]
                            del arr_yellow[:]
                            redcount = 0
                            purplecount = 0
                            greencount = 0
                            yellowcount = 0
                            arr_blue.append(i)
                            bluecount += 1
                        elif choose == PURPLE:
                            del arr_blue[:]
                            del arr_red[:]
                            del arr_green[:]
                            del arr_yellow[:]
                            bluecount = 0
                            redcountcount = 0
                            greencount = 0
                            yellowcount = 0
                            arr_purple.append(i)
                            purplecount += 1
                        elif choose == GREEN:
                            del arr_blue[:]
                            del arr_purple[:]
                            del arr_red[:]
                            del arr_yellow[:]
                            bluecount = 0
                            purplecount = 0
                            redcount = 0
                            yellowcount = 0
                            arr_green.append(i)
                            greencount += 1
                        elif choose == YELLOW:
                            del arr_blue[:]
                            del arr_purple[:]
                            del arr_green[:]
                            del arr_red[:]
                            bluecount = 0
                            purplecount = 0
                            greencount = 0
                            redcount = 0
                            arr_yellow.append(i)
                            yellowcount += 1


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

            print(x, y)

            del color
        #we have to delete the pixel array object after use otherwise it will give error like
                #surface is blocked









    pygame.display.update()


