import pygame
import random
from sprite import *

# This class creates obstacles
class Obstacle(Sprite):

    def __init__(self, game, x, y, width, name, screen_width, screen_height):
        sprite_position = 0
        type = 'obstacle'
        self.collided = False
        self.x_positions = [120, 368, 616]
        self.texture = pygame.image.load('./assets/obstacle.png') 
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, screen_width, screen_height)


    def choose_random_x(self):
       return self.x_positions[random.randrange(0, 3)]