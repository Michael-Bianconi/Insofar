"""Player"""

import pygame
from settings import BOTTOM,TOP,LEFT,RIGHT,BORDER_BUFFER

class Player(object):
	
	x = int(BOTTOM / 2)
	y = int(RIGHT / 2)
	v_speed = 0
	h_speed = 0
	velocity = 5
	color = (0,0,0)
	size = 10
	center = [x + int(size/2),y + int(size/2)]
	lasers = []
	
	def draw(self,screen):
		"""Draw to screen"""
		pygame.draw.ellipse(screen,self.color,[self.x,
											   self.y,
											   self.size,
											   self.size]
		)
	
	def tick(self):
		#move
		self.x += int(self.h_speed * self.velocity)
		self.y += int(self.v_speed * self.velocity)
		#print(str(self.x) + ' ' + str(self.y))
		#check bounds
		if self.x < LEFT + BORDER_BUFFER * 2:
			self.x = LEFT + BORDER_BUFFER * 2
		elif self.x + self.size > RIGHT - BORDER_BUFFER:
			self.x = RIGHT - self.size - BORDER_BUFFER
		if self.y < TOP + BORDER_BUFFER * 2:
			self.y = TOP + BORDER_BUFFER * 2
		elif self.y + self.size > BOTTOM - BORDER_BUFFER:
			self.y = BOTTOM - self.size - BORDER_BUFFER
		#update center
		self.center[0] = self.x + int(self.size/2)
		self.center[1] = self.y + int(self.size/2)
		#print('position: %s\r' % self.center, end='')
		
	def collision(self,asteroid):
		#compare the distance to combined radii
		dx = asteroid.center[0] - self.center[0]
		dy = asteroid.center[1] - self.center[1]
		radii = self.size / 2 + asteroid.size / 2
		
		if ((dx * dx) + (dy * dy) < radii * radii):
			return True
			
		else:
			return False