

import pygame

screen_width = 800
screen_height = 600

window = pygame.display.set_mode((screen_width, screen_height))


class Divider:

    def __init__(self, x, y):
        self.line_image = pygame.image.load('../assets/sprites.png')
        self.x = x
        self.y = y
        self.line_1_change = 1
        # window.fill('light blue')
    
    def load_divider(self):
        window.blit(self.line_image, (self.x, self.y))

divider = Divider(400, 20)

