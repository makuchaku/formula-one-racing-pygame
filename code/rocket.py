from sprite import *

# Rocket sprite
class Rocket(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 7
        type = 'rocket'
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)