from sprite import *

# Rocket sprite
class Life(Sprite):

    def __init__(self, game, x, y, width, name, screen_width, screen_height):
        self.window = pygame.display.set_mode((screen_width, screen_height))
        sprite_position = 0
        type = 'lives'
        self.heart_image = pygame.transform.scale(pygame.image.load('./assets/mcheart2.png'), (64, 64))
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, screen_width, screen_height)


    def draw_heart(self):
        self.window.blit(self.heart_image, (self.sprite_x, self.sprite_y))