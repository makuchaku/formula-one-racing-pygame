import pygame
from car import *
from rocket import *
from divider import *
import random
import time
from obstacle import *
from life import *

screen_width = 800
screen_height = 600

sprite_box = 64
speed = 1000
num_sprites = 5
car_move_sprite = 248


tanks = []
rockets = []
dividers = []
cars = []
lives = []
obstacle_start_x = 300


class Game:

    def __init__(self):
        self.energy_released = 0

        # Init pygame
        pygame.font.init()
        window = pygame.display.set_mode((screen_width, screen_height))
        window.fill('light blue')
        self.obstacle1 = Obstacle(self, 0, obstacle_start_x, obstacle_start_x, sprite_box, "Obstacle1") 
        self.obstacle2 = Obstacle(self, 0, obstacle_start_x, obstacle_start_x, sprite_box, "Obstacle2")
        # Init sound
        pygame.mixer.init()
        self.car = None

 
    # Creates all sprites
    def create_sprites(self):
        self.car = Car(self, (screen_width-sprite_box)/2, screen_height, 1)
    
        
        for i in range(3):
            divider1 = Divider(self, 400, 20, 64,64, i)
            divider2 = Divider(self, 400, 20, 64, 64, i)
            divider3 = Divider(self, 400, 20, 64, 64, i)
            life1 = Life(self, 112, 24, 64, 64, i)
            life2 = Life(self, 112 - 44, 24, 64, 64, i)
            life3 = Life(self, 112 - 44 * 2, 24, 64, 64, i)

            if i == 0:
                divider1.draw_divider(1 * 248, 20)
                divider2.draw_divider(1 * 248, 300)
                divider3.draw_divider(1 * 248, 600)
                life1.draw_heart()
                life2.draw_heart()
                life3.draw_heart()

            else:
                divider1.draw_divider(2 * 248, 20)
                divider2.draw_divider(2 * 248, 300)
                divider3.draw_divider(2 * 248, 600)
            dividers.append(divider1)
            dividers.append(divider2)
            dividers.append(divider3)
            lives.append(life1)
            lives.append(life2)
            lives.append(life3)


            self.car.load()
            cars.append(self.car)


    # Each iteration is a frame
    def render_frames(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if self.car.sprite_x == 616 and event.key == pygame.K_RIGHT:
                    self.car.play_sound("no_move")
                    # Don't move, already at right boundary
                    pass
                elif self.car.sprite_x == 120 and event.key == pygame.K_LEFT:
                    self.car.play_sound("no_move")
                    # Don't move, already at left boundary
                    pass
                elif event.key == pygame.K_RIGHT and self.car.sprite_x != 616:
                    self.car.play_sound("move")
                    self.car.move_x(car_move_sprite)
                elif event.key == pygame.K_LEFT and self.car.sprite_x != 120:
                    self.car.play_sound("move")
                    self.car.move_x(-car_move_sprite)



            # Cleans the screen
            ## ONLY DO THIS BEFORE RENDERING ALL SPRITES
            window.fill('light blue')

            # Set up all positions
            # self.car.move_y(-1)
            # time.sleep(1/speed)
            self.car.draw()

            # Draw obstacles
            self.obstacle1.draw()
            self.obstacle2.draw()


            for divider in dividers:
                divider.move_y(1)
                self.car.distance_travelled = round(self.car.distance_travelled + 1/100, 2)

            # Render dividers
            for divider in dividers:
                divider.draw_divider(divider.sprite_x, divider.sprite_y)

            if self.obstacle1.sprite_y == screen_height:
                self.obstacle1.sprite_y = obstacle_start_x
            else:
                self.obstacle1.sprite_y += 1


            if self.obstacle2.sprite_y == screen_height:
                self.obstacle2.sprite_y = obstacle_start_x
            else:
                self.obstacle2.sprite_y += 1

            for a_life in lives:

                a_life.draw_heart()

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
            #                         self.play_sound('punch')
            #                         print('Sprite Energy', sprite.energy, 'Other Sprite Energy', other_sprite.energy)
            #                 elif sprite.type != other_sprite.type:
            #                     if sprite.killed == False and other_sprite.killed == False:
            #                         self.energy_released += (sprite.energy + other_sprite.energy)
            #                         sprite.kill_sprite()
            #                         other_sprite.kill_sprite()
            #                         self.play_sound("explosion")
                        
            for divider in dividers:
                if divider.sprite_y == screen_height:
                    divider.sprite_y = 0
                    self.obstacle1.sprite_x = self.obstacle1.choose_random_x()
                    self.obstacle2.sprite_x = self.obstacle2.choose_random_x()

            self.show_message(str(self.car.distance_travelled), (screen_width/2, 50))
            self.show_message(str(self.car.lives), (screen_width - 100, 50))

            # Display everything
            pygame.display.update()


    def stop(self):
        pygame.quit()
    
    
    def play_sound(self, sound_name):
        pygame.mixer.Sound('./assets/' + sound_name + '.wav').play()

    
    def show_message(self, message, spot):
        # sets the font and color
        font = pygame.font.SysFont('timesnewroman',  60)
        green = 0, 0, 255
        text = font.render(message, True, green)
        textRect = text.get_rect()
        #puts the score at the center of the screen
        textRect.center = (spot)
        window.blit(text, textRect)
        pygame.display.flip()

