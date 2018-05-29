"""lasers"""
import pygame
import time
from math import sin, cos, pi
from settings import LASER_DURATION,BOTTOM,TOP,LEFT,RIGHT

class Laser(object):
	
	start = [0,0]
	angle = pi/2 #radians
	end = [0,0]
	color = (255,0,0)
	creation_time = 0
	
	
	def __init__(self,start,angle):
		#startpoint
		self.start = start
		#distance from barriers
		self.end = Laser.end_point(start,angle)
		#duration
		self.creation_time = time.time()
		
	def end_point(point,angle):
		#print('angle %s\r' % str(angle),end='')
		#cardinal direction (avoid divide by zero)
		if angle == 0: return [RIGHT,point[1]]
		if angle == pi/2: return [point[0],TOP]
		if angle == pi: return [LEFT,point[1]]
		if angle == 3*pi/2: return [point[0],BOTTOM]

		s = sin(angle)
		c = cos(angle)
		
		#north,south,east,west
		bounds = [(TOP-point[1])/s,
				  (BOTTOM-point[1])/s,
				  (RIGHT-point[0])/c,
				  (LEFT-point[0])/c
		]
		
		#find smallest positive bound
		try:
			t = min(b for b in bounds if b > 4)
		except ValueError:
			return [0,0]
		#return coordinate
		return [point[0]+t*c,point[1]+t*s]
		
	def end_of_life(self):
		if time.time() - self.creation_time > LASER_DURATION:
			return True
		return False
		
	def draw(self,screen):
		pygame.draw.line(screen,self.color,self.start,self.end,8)
		