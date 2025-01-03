import pygame
from sprite import *
from game import *

# Car sprite
class Car(Sprite):

    def __init__(self, game, x, y, name, screen_width, screen_height):
        sprite_position = 0
        type = 'car'
        self.distance_travelled = 0
        self.lives = 3
        self.width = 84
        self.height = 84
        self.texture =  pygame.transform.scale(pygame.image.load('./assets/car1.png'), (self.width, self.height))
        pygame.mixer.music.load('assets/car_racing_sound.mp3')
        pygame.mixer.music.play(-1, 0.0)
        Sprite.__init__(self, game, x -10, y - 20, self.width, self.height, sprite_position, name, type, screen_width, screen_height)
        

    def play_sound(self, type):
        if type == "no_move":
            self.game.play_sound("no_move")

        if type == "move":
            self.game.play_sound("move")
        
        if type == "collision":
            self.game.play_sound("explosion")

    def crashed(self):
        self.lives -= 1
        pygame.mixer.music.pause()
        pygame.time.delay(300)
        pygame.mixer.music.play()
        if self.lives == 0:
           pygame.mixer.music.stop() 
