__author__ = 'samirpatil'


import pygame, sys
from pygame.locals import *



pygame.init()
clock = pygame.time.Clock()

FRAMES = 30
# mouse button
LEFT = 1
# nxn matrix
n = 5
#arrays and counts for all the used colours (used to undo the last step)

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




def main(c1, c2, c3, c4, c5):

    # variables for storing coordinates of point clicked
    x = 0
    y = 0
    # creation of a static level
    """
    c1 = Red
    c2 = Green
    c3 = Blue
    c4 = Purple
    c5 = Orange
    """
    c1last = c1.__len__() - 1
    c2last = c2.__len__() - 1
    c3last = c3.__len__() - 1
    c4last = c4.__len__() - 1
    c5last = c5.__len__() - 1

    fill[c1[c1last]].fill(RED)
    fill[c1[0]].fill(RED)

    fill[c2[c2last]].fill(GREEN)
    fill[c2[0]].fill(GREEN)

    fill[c3[c3last]].fill(BLUE)
    fill[c3[0]].fill(BLUE)

    fill[c4[c4last]].fill(PURPLE)
    fill[c4[0]].fill(PURPLE)

    fill[c5[c5last]].fill(ORANGE)
    fill[c5[0]].fill(ORANGE)

    # arrays for storing the coloured squares , useful for implementing UNDO and Restart
    arr_red = []
    arr_blue = []
    arr_green = []
    arr_orange = []
    arr_purple = []
    bluecount = 0
    redcount = 0
    greencount = 0
    orangecount = 0
    purplecount = 0

    undocount = 0
    stars = 0

    #variable for identification of dragging event
    isDragging = 0

    b1 = button("UNDO")
    b1.button_coordinates(0, n*75, 75, 75)
    b1.place_button(pygame.image.load('undo1.png'))

    b2 = button("RESTART")
    b2.button_coordinates(75, n*75, 75, 75)
    b2.place_button(pygame.image.load('restart.png'))

    # flags to avoid repeated checking of a colour path completion
    flagred = False
    flagblue = False
    flaggreen = False
    flagorange = False
    flagpurple = False



    # Winning condition counter, counts each bridge
    win_count = 0

    # run the game loop
    while True:
        clock.tick(FRAMES)
        # testing purpose


        for county in range(0, n):
            for countx in range(0, n):
                  DISPLAYSURF.blit(fill[n*county+countx], (countx*75, county*75))

        dline()

        for event in pygame.event.get():
            if event.type == QUIT:
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


                elif color[x, y] == DISPLAYSURF.map_rgb(PURPLE):
                    isDragging = 1
                    choose = PURPLE
                    del color


                elif color[x, y] == DISPLAYSURF.map_rgb(BLUE):
                    isDragging = 1
                    choose = BLUE
                    del color

                elif color[x, y] == DISPLAYSURF.map_rgb(ORANGE):
                    isDragging = 1
                    choose = ORANGE
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
                # when undo is clicked
                if b1.rect.collidepoint(x, y):
                    print "i am in"
                    undocount += 1
                    del color
                    while bluecount > 0:
                        fill[arr_blue[bluecount-1]].fill(BLACK)
                        print arr_blue
                        arr_blue.pop(-1)
                        bluecount -= 1
                        # now as undo is clicked we have to decrement the win count and also reset the colour check flag but only one time



                    while redcount > 0:
                        print redcount
                        fill[arr_red[redcount-1]].fill(BLACK)
                        arr_red.pop(-1)
                        redcount -= 1


                    while purplecount > 0:
                        fill[arr_purple[purplecount-1]].fill(BLACK)
                        arr_purple.pop(-1)
                        purplecount -= 1

                    while greencount > 0:
                        fill[arr_green[greencount-1]].fill(BLACK)
                        arr_green.pop(-1)
                        greencount -= 1


                    while orangecount > 0:
                        fill[arr_orange[orangecount-1]].fill(BLACK)
                        arr_orange.pop(-1)
                        orangecount -= 1



                    b1.place_button(pygame.image.load('undo1.png'))
                # when restart is clicked
                elif b2.rect.collidepoint(x, y):
                    undocount = 0
                    del color
                    for d in range(0, n*n):
                        fill[d].fill(BLACK)

                    fill[c1[c1last]].fill(RED)
                    fill[c1[0]].fill(RED)

                    fill[c2[c2last]].fill(GREEN)
                    fill[c2[0]].fill(GREEN)

                    fill[c3[c3last]].fill(BLUE)
                    fill[c3[0]].fill(BLUE)

                    fill[c4[c4last]].fill(PURPLE)
                    fill[c4[0]].fill(PURPLE)

                    fill[c5[c5last]].fill(ORANGE)
                    fill[c5[0]].fill(ORANGE)

                    b2.place_button(pygame.image.load('restart.png'))

                    del arr_blue[:]
                    del arr_purple[:]
                    del arr_green[:]
                    del arr_orange[:]
                    del arr_red[:]
                    bluecount = 0
                    purplecount = 0
                    greencount = 0
                    redcount = 0
                    orangecount = 0
                    win_count = 0

                    flagred = False
                    flagblue = False
                    flaggreen = False
                    flagorange = False
                    flagpurple = False



                else:
                    del color
                print("mouse button is up")



            if event.type == pygame.MOUSEMOTION and isDragging == 1:

                color = pygame.PixelArray(DISPLAYSURF)
                x, y = event.pos
                if color[x, y] == DISPLAYSURF.map_rgb(BLACK):
                    for i in range(0, n*n):
                        if check[i].collidepoint(x, y):
                            fill[i].fill(choose)
                            prevx = x
                            prevy = y
                            # now we keep a list of latest filled square to undo them, we also delete the last coloured entries
                            if choose == RED:
                                bluecount = 0
                                purplecount = 0
                                greencount = 0
                                orangecount = 0
                                arr_red.append(i)
                                print arr_red
                                redcount += 1

                            elif choose == BLUE:
                                redcount = 0
                                purplecount = 0
                                greencount = 0
                                orangecount = 0
                                arr_blue.append(i)
                                bluecount += 1

                            elif choose == PURPLE:
                                bluecount = 0
                                redcount = 0
                                greencount = 0
                                orangecount = 0
                                arr_purple.append(i)
                                purplecount += 1

                            elif choose == GREEN:
                                bluecount = 0
                                purplecount = 0
                                redcount = 0
                                orangecount = 0
                                arr_green.append(i)
                                greencount += 1

                            elif choose == ORANGE:
                                bluecount = 0
                                purplecount = 0
                                greencount = 0
                                redcount = 0
                                arr_orange.append(i)
                                orangecount += 1


                elif color[x, y] == DISPLAYSURF.map_rgb(BLUE) and not choose == BLUE:
                    pygame.mouse.set_pos(prevx, prevy)

                elif color[x, y] == DISPLAYSURF.map_rgb(RED) and not choose == RED:
                    pygame.mouse.set_pos(prevx, prevy)

                elif color[x, y] == DISPLAYSURF.map_rgb(PURPLE) and not choose == PURPLE:
                    pygame.mouse.set_pos(prevx, prevy)

                elif color[x, y] == DISPLAYSURF.map_rgb(ORANGE) and not choose == ORANGE:
                    pygame.mouse.set_pos(prevx, prevy)

                elif color[x, y] == DISPLAYSURF.map_rgb(GREEN) and not choose == GREEN:
                    pygame.mouse.set_pos(prevx, prevy)



                del color
            #we have to delete the pixel array object after use otherwise it will give error like
                    #surface is blocked

        tot = arr_red.__len__() + arr_green.__len__() + arr_blue.__len__() + arr_orange.__len__() + arr_purple.__len__()
        if tot == n*n - n*2:
            if arr_red.__len__() == c1.__len__() - 2 and not flagred:

                for i in range(0, arr_red.__len__()):
                    if (arr_red[i] == c1[i+1]) or (arr_red[i] == c1[(c1last-1)-i]):

                        if i == arr_red.__len__() - 1:
                            flagred = True
                            win_count += 1
                            #print win_count
                        continue
                    else:
                        break

            if arr_green.__len__() == c2.__len__() - 2 and not flaggreen:

                for i in range(0, arr_green.__len__()):
                    if (arr_green[i] == c2[i+1]) or (arr_green[i] == c2[(c2last-1)-i]):

                        if i == arr_green.__len__() - 1:
                            flaggreen = True
                            win_count += 1
                            #print win_count
                        continue
                    else:
                        break

            if arr_blue.__len__() == c3.__len__() - 2 and not flagblue:

                for i in range(0, arr_blue.__len__()):
                    if (arr_blue[i] == c3[i+1]) or (arr_blue[i] == c3[(c3last-1)-i]):

                        if i == arr_blue.__len__() - 1:
                            flagblue = True
                            win_count += 1
                            #print win_count
                        continue
                    else:
                        break

            if arr_purple.__len__() == c4.__len__() - 2 and not flagpurple:

                for i in range(0, arr_purple.__len__()):
                    if (arr_purple[i] == c4[i+1]) or (arr_purple[i] == c4[(c4last-1)-i]):

                        if i == arr_purple.__len__() - 1:
                            flagpurple = True
                            win_count += 1
                            #print win_count
                        continue
                    else:
                        break

            if arr_orange.__len__() == c5.__len__() - 2 and not flagorange:

                for i in range(0, arr_purple.__len__()):
                    if (arr_orange[i] == c5[i+1]) or (arr_orange[i] == c5[(c5last-1)-i]):

                        if i == arr_orange.__len__() - 1:
                            flagorange = True
                            win_count += 1
                           # print win_count
                        continue
                    else:
                        break


        if win_count >= 5:
            win_count = 0
            print "hurray !!!!"

            if undocount >= 4:
                stars = 1
            else:
                stars = 5-undocount

            print stars
        datafile = open('stardata.txt', 'w')
        datafile.write(str(stars))
        pygame.display.update()

