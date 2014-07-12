import pygame, os
import random
height = 500
width = 1000
y = 50
change = 1
color = [0, 0, 0]
color_change = [1, 1, 1, 1]
dimensions = (width, height)
direct = [0.5, 0.5, 1, 1]
screen = pygame.display.set_mode(dimensions)
running = 1
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((0, 0, 0))
	img = pygame.image.load(os.path.join("resources", "Helicopter.png"))
	screen.blit(img, (25,y))
	y += change
	x = pygame.mouse.get_pressed()[0]
	
	if y == 5 or y == height-5:
		raise Exception("You lost :( ")
	if x == 1:
		change = -1
	else:
		change = 1
	
	pygame.display.flip()
	
	
