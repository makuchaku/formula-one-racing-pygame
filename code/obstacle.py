import pygame
import random
from sprite import *

# This class creates obstacles
class Obstacle(Sprite):

    def __init__(self, game, x, y, width, height, name, screen_width, screen_height):
        sprite_position = 0
        type = 'obstacle'
        self.collided = False
        self.x_positions = [120, 368, 616]
        self.obstacle_start_y = y
        x = self.choose_random_x()
        self.texture = pygame.image.load('./assets/obstacle.png') 
        Sprite.__init__(self, game, x, y, width, height, sprite_position, name, type, screen_width, screen_height)


    def choose_random_x(self):
       return self.x_positions[random.randrange(0, 3)]