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
    """Contains all the functions and variables that only the helicopter needs"""
    def __init__(self, screen):
        """Creates all the essential variables"""
        self.change = 1
        self.y = 50
        self.img = pygame.image.load(os.path.join("resources", "Helicopter.png"))
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
        self.screen.blit(self.img, (25, self.y))

#The user's helicopter
heli = Helicopter(window)


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
    #shows the helicopter
    heli.blit()

    #updates the display
    pygame.display.flip()
    
    
