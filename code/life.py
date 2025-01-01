from sprite import *

# Rocket sprite
class Life(Sprite):

    def __init__(self, game, x, y, width, name):
        sprite_position = 0
        type = 'lives'
        self.heart_image = pygame.transform.scale(pygame.image.load('./assets/mcheart2.png'), (64, 64))
        Sprite.__init__(self, game, x, y, width, sprite_position, name, type, 0)


    def draw_heart(self):
        window.blit(self.heart_image, (self.sprite_x, self.sprite_y))