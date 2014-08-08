#import modules
import pygame
import os
import random
import time
def main():
	#create the screen
	height = 500
	width = 1000
	dimensions = (width, height)
	window = pygame.display.set_mode(dimensions)

	#helps with making the close button in the corner work
	running = 1

	class Box:
		def __init__(self, width, height):
			self.width = width
			self.height = height
			self.box = []
		def makeBox(self):
			pass		
	class Helicopter:
		"""Contains all the functions and variables that only the helicopter needs"""
		def __init__(self, screen):
			"""Creates all the essential variables"""
			self.change = 1
			self.y = 50
			self.x = 25
			self.img = pygame.image.load(os.path.join("/usr/share/heligame/resources", "Helicopter.png"))
			self.click = 0
			self.screen = screen
		def move(self):
			"""Moves the helicopter if computer detects left-click"""
			self.click = pygame.mouse.get_pressed()[0]
			if self.click == 1:
				self.change = -1
			else:
				self.change = 1
			self.y += self.change
		def blit(self):
			"""Displays the helicopter"""
			self.screen.blit(self.img, (self.x, self.y))

	class Obstacle:
		"""Contains all the functions and variables specific to the boxes"""
		def __init__(self, screen):
			self.change = 4
			self.y = random.randrange(0, 560)
			self.x = 999
			self.img = pygame.image.load(os.path.join("/usr/share/heligame/resources", "Obstacle.png"))
			self.screen = screen
		def move(self):
			"""Moves the murderous obstacle towards its destination's x point"""
			self.x -= self.change
			if self.x <= 1:
				self.x = 999
				self.y = random.randrange(0, 560)
		def blit(self):
			"""Makes the user able to see and thus evade the obstacle"""
			self.screen.blit(self.img, (self.x, self.y))        
		

	#The user's helicopter
	heli = Helicopter(window)
	obs = [Obstacle(window), Obstacle(window), Obstacle(window)]

		
		
	score = 0
	#gameloop
	while running:
		
		#makes the close button functional
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		
		#makes the background black 
		window.fill((0, 0, 0))
		
		
		#moves the helicopter
		heli.move()
		obs[0].move()
		obs[1].move()
		obs[2].move()
		
		
		#shows the helicopter
		heli.blit()
		obs[0].blit()
		obs[1].blit()
		obs[2].blit()

		if heli.y <= 1 or heli.y >= 500:
			break
		
		if heli.y in range(obs[0].y, obs[0].y + 40) and heli.x in range(obs[0].x, obs[0].x + 64):
			break
			
		elif heli.y in range(obs[1].y, obs[1].y + 40) and heli.x in range(obs[1].x, obs[1].x + 64):
			break
			
		elif heli.y in range(obs[2].y, obs[2].y + 40) and heli.x in range(obs[2].x, obs[2].x + 64):
			break  
		#updates the display
		pygame.display.flip()
if __name__ == '__main__':
	main()
		
