import pygame
from sprite import *
from game import *

# Car sprite
class Car(Sprite):

    def __init__(self, game, x, y, width, name, screen_width, screen_height):
        sprite_position = 0
        type = 'car'
        self.distance_travelled = 0
        self.lives = 3
        self.texture =  pygame.transform.scale(pygame.image.load('./assets/car1.png'), (64, 64))
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, screen_width, screen_height)
        

    def play_sound(self, type):
        if type == "no_move":
            self.game.play_sound("no_move")

        if type == "move":
            self.game.play_sound("move")
        
        if type == "collision":
            self.game.play_sound("explosion")

    def lose_life(self):
        self.lives -= 1