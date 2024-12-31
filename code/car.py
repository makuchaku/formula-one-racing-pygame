import pygame
from sprite import *
from game import *


# Car sprite
class Car(Sprite):

    def __init__(self, game, x, screeHeight, name):
        sprite_position = 0
        type = "car"
        width = 74
        height = 102
        self.distance_travelled = 0
        self.lives = 3
        Sprite.__init__(self, game, x, screeHeight-height, width, height, sprite_position, name, type, 0)
        self.texture = pygame.transform.scale(pygame.image.load("./assets/car1.png"), (width, height))

    def play_sound(self, type):
        if type == "no_move":
            self.game.play_sound("no_move")

        if type == "move":
            self.game.play_sound("move")

        if type == "collision":
            self.game.play_sound("explosion")

    def lose_life(self):
        self.lives -= 1
