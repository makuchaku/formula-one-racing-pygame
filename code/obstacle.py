from sprite import *

# This class creates obstacles
class Obstacle(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 0
        type = 'obstacle'
        self.x_positions = [120, 368, 616]
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)


    def choose_random_x(self):
       return self.x_positions[random.randrange(0, 3)]
