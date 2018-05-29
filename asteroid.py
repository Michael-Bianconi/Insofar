"""asteroids"""

import pygame, random
from settings import ASTEROID_COLOR, ASTEROID_DAMAGE_RATE, DEATH_COLOR
from settings import LEFT,RIGHT,TOP,BOTTOM,BORDER_BUFFER

class Asteroid(object):

	x = 0
	y = 0
	size = 0
	center = [x+int(size/2),y+int(size/2)]
	h_speed = 3
	v_speed = 3
	#size = random.randint(10,100)
	color = ASTEROID_COLOR

	def __init__(self):

		#random size
		size = random.randint(20,200)
		
		#determine which side to spawn on
		s = random.randint(0,4)
		
		if s == 0:
			self.y = TOP + BORDER_BUFFER
			self.x = random.randint(LEFT + BORDER_BUFFER,RIGHT - BORDER_BUFFER)
		elif s == 1:
			self.y = BOTTOM - BORDER_BUFFER - self.size
			self.x = random.randint(LEFT + BORDER_BUFFER,RIGHT - BORDER_BUFFER)
		elif s == 2:
			self.y = random.randint(TOP + BORDER_BUFFER,BOTTOM - BORDER_BUFFER)
			self.x = RIGHT - BORDER_BUFFER - self.size
		elif s == 3:
			self.y = random.randint(TOP + BORDER_BUFFER,BOTTOM - BORDER_BUFFER)
			self.x = LEFT + BORDER_BUFFER
			
		#speed
		self.h_speed = random.randint(1,3)
		self.v_speed = random.randint(1,3)
		
		self.size = size
		self.center = [self.x+int(self.size/2),self.y+int(self.size/2)]
	
	def draw(self,screen):
	
		if self.size > 10:
			"""Draw to screen"""
			pygame.draw.ellipse(screen,self.color,[self.x,
												   self.y,
												   self.size,
												   self.size]
			)
		
	def tick(self):
		self.x += self.h_speed
		self.y += self.v_speed
		
		
		if self.x < LEFT + BORDER_BUFFER * 2:
			self.x = LEFT + BORDER_BUFFER * 2
			self.h_speed = -self.h_speed
		elif self.x + self.size > RIGHT - BORDER_BUFFER:
			self.x = RIGHT - self.size - BORDER_BUFFER
			self.h_speed = -self.h_speed
		if self.y < TOP + BORDER_BUFFER * 2:
			self.y = TOP + BORDER_BUFFER * 2
			self.v_speed = -self.v_speed
		elif self.y + self.size > BOTTOM - BORDER_BUFFER:
			self.y = BOTTOM - self.size - BORDER_BUFFER
			self.v_speed = -self.v_speed
			
		#update center
		self.center[0] = self.x + int(self.size/2)
		self.center[1] = self.y + int(self.size/2)
		
	def laser_collision(self,laser):
		
		#point slope form: y - y1 = m(x - x1)
		#slope
		def point_slope(laser,x):
			m = (laser.end[1]-laser.start[1])/(laser.end[0]-laser.start[0])
			return laser.start[1] + m * (x - laser.start[0])
		
		# for quadrant
		if laser.start[0] < laser.end[0]:
			start = laser.start[0]
			end = laser.end[0]
		else:
			start = laser.end[0]
			end = laser.start[0]
			
		while start < end:
			#point is on the correct x plane
			#print(start)
			if self.x+self.size > start > self.x:
				y = point_slope(laser,start)
				#print(y)
				if self.y+self.size > y > self.y:
					return True
			start += 1
		
		return False
		
	def damage(self):
		if self.size > 10:
			self.size -= ASTEROID_DAMAGE_RATE
		else:
			self.size = 0
			self.color = DEATH_COLOR
			
def spawn(list):
	list.append(Asteroid())