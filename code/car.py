from sprite import *

# Car sprite
class Car(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 2
        type = 'car'
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)
