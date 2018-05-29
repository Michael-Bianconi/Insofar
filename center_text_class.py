"""Center Text"""

import pygame
pygame.font.init()
from settings import SCREEN_HEIGHT,SCREEN_WIDTH

class CenterText():

	text = ''
	font = pygame.font.SysFont('calibri', 25, True, False)
	coord = [int(SCREEN_WIDTH / 2),int(SCREEN_HEIGHT / 2)]
	
	def __init__(self,text,color):
		self.text = self.font.render(text,True,color)
		
	def draw(self,screen):
		screen.blit(self.text,self.coord)