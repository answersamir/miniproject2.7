
import pygame, sys
from pygame.locals import *
from time import sleep


pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Start')

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

DISPLAYSURF.fill(BLACK)



for i in range (0, 10):
            pygame.draw.rect(DISPLAYSURF, YELLOW, [0, i*50, 50, (i+1)*50])
            pygame.display.flip()
            sleep(0.5)

while True:



    for event in pygame.event.get():
        fpsClock.tick(FPS)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()







