from sprite import *


class Car(Sprite):
    def __init__(self, x, y, width, name):
        sprite_position = 0
        sprite = "car"
        Sprite.__init__(self, x, y, width, sprite_position, name, type, 0)
