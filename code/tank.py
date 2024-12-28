from sprite import *

# Tank sprite
class Tank(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 0
        type = 'tank'
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)