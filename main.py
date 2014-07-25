#import modules
import pygame
import os
import random
import time
#create the screen
height = 500
width = 1000
dimensions = (width, height)
window = pygame.display.set_mode(dimensions)

#helps with making the close button in the corner work
running = 1

class Helicopter:
    """Contains all the functions and variables that only the helicopter needs"""
    def __init__(self, screen):
        """Creates all the essential variables"""
        self.change = 1
        self.y = 50
        self.x = 25
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
        self.screen.blit(self.img, (self.x, self.y))

class Obstacle:
    """Contains all the functions and variables specific to the boxes"""
    def __init__(self, screen):
        self.change = 4
        self.y = random.randrange(0, 560)
        self.x = 999
        self.img = pygame.image.load(os.path.join("resources", "Obstacle.png"))
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
obs1 = Obstacle(window)
obs2 = Obstacle(window)
obs3 = Obstacle(window)

    
    
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
    obs1.move()
    obs2.move()
    obs3.move()
    
    
    #shows the helicopter
    heli.blit()
    obs1.blit()
    obs2.blit()
    obs3.blit()

    if heli.y <= 1 or heli.y >= 500:
        break
    
    if heli.y in range(obs1.y, obs1.y + 40) and heli.x in range(obs1.x, obs1.x + 64):
        break
        
    elif heli.y in range(obs2.y, obs2.y + 40) and heli.x in range(obs2.x, obs2.x + 64):
        break
        
    elif heli.y in range(obs3.y, obs3.y + 40) and heli.x in range(obs3.x, obs3.x + 64):
        break  
    #updates the display
    pygame.display.flip()
    
    
