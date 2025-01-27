from pygame.locals import *
from gamestart import *
from game import *

screen_width = 800
screen_height = 600

game_start = GameStart(screen_width, screen_height)
player_name = game_start.get_user_name()
game = Game(player_name, screen_width, screen_height)
game.create_sprites()
game.render_frames()
game.stop()