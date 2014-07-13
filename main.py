#import modules
import pygame
import os
import random

#create the screen
height = 500
width = 1000
dimensions = (width, height)
window = pygame.display.set_mode(dimensions)
running = 1

class Helicopter:
    def __init__(self, screen):
        self.change = 1
        self.y = 50
        self.img = pygame.image.load(os.path.join("resources", "Helicopter.png"))
        self.click = 0
        self.screen = screen
    def move(self):
        self.click = pygame.mouse.get_pressed()[0]
        if self.click == 1:
            self.change = -1
        else:
            self.change = 1
        self.y += self.change
    def blit(self):
        self.screen.blit(self.img, (25, self.y))
heli = Helicopter(window)

while running:
    #makes the close button functional
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    
    #makes the background black 
    window.fill((0, 0, 0))
    
    heli.move()
    heli.blit()

    pygame.display.flip()
    
    
