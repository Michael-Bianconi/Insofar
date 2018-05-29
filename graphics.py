import pygame, random
from math import pi, atan2
from settings import SCREEN_HEIGHT,SCREEN_WIDTH,BACKGROUND_COLOR
from settings import ASTEROID_SPAWN_RATE, NUM_STARS
from laser import Laser
from player import Player
from asteroid import Asteroid,spawn
from repeated_timer import RepeatedTimer
from center_text_class import CenterText

pygame.display.init()
pygame.joystick.init()
clock = pygame.time.Clock()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Insofar')
exit = False

player = Player()

lasers = []
asteroids = []

stars_x = random.sample(range(0,SCREEN_WIDTH), NUM_STARS)
stars_y = random.sample(range(0,SCREEN_HEIGHT),NUM_STARS)

asteroid_timer = RepeatedTimer(ASTEROID_SPAWN_RATE,spawn,asteroids)

death = False
death_text = CenterText('You died!', (255,255,0))

while exit is False:

	joystick_count = pygame.joystick.get_count()
	
	if joystick_count == 0:
		print('Missing joystick!')
		exit = True
		
	else:
		move_joystick = pygame.joystick.Joystick(0)
		move_joystick.init()

		h_axis = move_joystick.get_axis(0)
		v_axis = move_joystick.get_axis(1)
		
		player.h_speed = h_axis
		player.v_speed = v_axis

		
		
		if h_axis != 0:
			angle = atan2(v_axis,h_axis)
		
			lasers.append(Laser([player.x,player.y],angle))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
	
	screen.fill(BACKGROUND_COLOR)
	
	#draw stars
	for i,x in enumerate(stars_x):
		pygame.draw.ellipse(screen,(255,255,255),[x,stars_y[i],3,3])
		
	if death is False:
		for i, l in enumerate(lasers):
			if l.end_of_life():
				del lasers[i]
			else:
				l.draw(screen)
				for i, a in enumerate(asteroids):
					if a.laser_collision(l):
						a.damage()
						if a.size == 0:
							del asteroids[i]
	
	else:
		death_text.draw(screen)
	
	for a in asteroids:
		a.tick()
		a.draw(screen)
		if player.collision(a):
			death = True
	
	player.tick()
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
asteroid_timer.stop()