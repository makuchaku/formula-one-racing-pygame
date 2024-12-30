from sprite import *

class Obstacle(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 2
        type = 'obstacle'
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)

