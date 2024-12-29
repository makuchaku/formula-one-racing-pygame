import pygame
from car import *
from rocket import *
from divider import *
import random
import time

# width_or_height = 500
screen_width = 800
screen_height = 600

sprite_box = 64
speed = 1000
num_sprites = 5

tanks = []
rockets = []
dividers = []


class Game:

    def __init__(self):
        self.energy_released = 0

        # Init pygame
        pygame.font.init()
        window = pygame.display.set_mode((screen_width, screen_height))
        window.fill('light blue')

        # Init sound
        pygame.mixer.init()
        self.car = None

    # Creates all sprites
    def create_sprites(self):
        self.car = Car(self, (screen_width-sprite_box)/2, (screen_height-sprite_box), sprite_box, 1)
        
        for i in range(3):
            divider1 = Divider(self, 400, 20, 64, i)
            divider2 = Divider(self, 400, 20, 64, i)
            divider3 = Divider(self, 400, 20, 64, i)
            if i == 0:
                divider1.draw_divider(1 * 248, 20)
                divider2.draw_divider(1 * 248, 300)
                divider3.draw_divider(1 * 248, 600)
            else:
                divider1.draw_divider(2 * 248, 20)
                divider2.draw_divider(2 * 248, 300)
                divider3.draw_divider(2 * 248, 600)
            dividers.append(divider1)
            dividers.append(divider2)
            dividers.append(divider3)


            car = Car(self, random.randint(10, screen_width),
                      random.randint(10, screen_height), 64, i)
            car.load()
            cars.append(car)

            car = Car(self, random.randint(10, screen_width),
                      random.randint(10, screen_height), 64, i)
            car.load()
            cars.append(car)

    # Each iteration is a frame
    def render_frames(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            # Cleans the screen
            ## ONLY DO THIS BEFORE RENDERING ALL SPRITES
            window.fill('light blue')

            # Set up all positions
            # self.car.move_y(-1)
            # time.sleep(1/speed)
            self.car.draw()

            for divider in dividers:
                divider.move_y(1)
                time.sleep(1/speed)

            # Render dividers
            for divider in dividers:
                divider.draw_divider(divider.sprite_x, divider.sprite_y)

            # # Checks for collisions
            # all_sprites = tanks + rockets
            # for sprite in all_sprites:
            #     for other_sprite in all_sprites:
            #         if sprite.name != other_sprite.name:
            #             if sprite.check_and_change_direction(other_sprite) == True:
            #                 if sprite.type == other_sprite.type:
            #                     if sprite.killed == False and other_sprite.killed == False:
            #                         sprite.energy += 1
            #                         other_sprite.energy += 1
            #                         self.play_sound('./assets/punch.wav')
            #                         print('Sprite Energy', sprite.energy, 'Other Sprite Energy', other_sprite.energy)
            #                 elif sprite.type != other_sprite.type:
            #                     if sprite.killed == False and other_sprite.killed == False:
            #                         self.energy_released += (sprite.energy + other_sprite.energy)
            #                         sprite.kill_sprite()
            #                         other_sprite.kill_sprite()
            #                         # pygame.mixer.music.load("explosion.wav")
            #                         # pygame.mixer.music.play(loops=1)
            #                         self.play_sound('./assets/explosion.wav')
                        
            for divider in dividers:
                if divider.sprite_y == screen_height:
                    divider.sprite_y = 0
                    print('resetting', divider.name, 'to 0')

            self.show_message(str(self.energy_released))

            # Display everything
            pygame.display.update()


    def stop(self):
        pygame.quit()
    
    
    def play_sound(self, sound):
         pygame.mixer.Sound(sound).play()

    
    def show_message(self, message):
        # print('showing text')
        #sets the font and color
        font = pygame.font.SysFont('timesnewroman',  60)
        green = 0, 0, 255
        text = font.render(message, True, green)
        textRect = text.get_rect()
        #puts the score at the center of the screen
        textRect.center = (50, 50)
        window.blit(text, textRect)
        pygame.display.flip()
        # time.sleep(3)
    