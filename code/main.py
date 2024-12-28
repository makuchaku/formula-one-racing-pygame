import pygame, sys
from pygame.locals import *
# from car import *
# from obstacle import *
# from game import *
# from sprite import *
# from tank import *
# import sprite
# import car
# import obstacle
from game import *
# import tank


game = Game()
game.create_sprites()
game.render_frames()
game.stop()



