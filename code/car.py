from sprite import *

# Car sprite
class Car(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 0
        type = 'car'
        self.distance_travelled = 0
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)
        

    def play_sound(self, type):
        if type == "no_move":
            self.game.play_sound("no_move")

        if type == "move":
            self.game.play_sound("move")
        
        if type == "collision":
            self.game.play_sound("explosion")