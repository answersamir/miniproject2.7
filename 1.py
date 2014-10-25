import pygame,sys
from pygame.locals import *

pygame.init()
RED = (255, 0, 0)
screen = pygame.display.set_mode((400,600))

obj = pygame.Surface((100,400))
obj1 = obj.convert_alpha()
obj1.fill(RED)
screen.blit(obj1,(50,50))

back = pygame.Surface((400,600))
back1 = back.convert_alpha()
back1.fill((0,200,0,100))

screen.blit(back1,(0,0))

while True :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.quit()
			
	pygame.display.update()		
