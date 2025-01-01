import pygame, sys
from pygame.locals import *
from game import *


game = Game()
game.create_sprites()
game.render_frames()
game.stop()



