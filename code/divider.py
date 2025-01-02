import pygame
from sprite import *

class Divider(Sprite):

    def __init__(self, game, x, y, width, name, screen_width, screen_height):
        self.window = pygame.display.set_mode((screen_width, screen_height))
        sprite_position = 0
        type = 'divider'
        self.line_image = pygame.image.load('./assets/line.png')
        self.line_1_change = 1
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, screen_width, screen_height)


    def draw_divider(self, x, y):
        self.sprite_x = x
        self.sprite_y = y
        self.window.blit(self.line_image, (x, y))