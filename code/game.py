import pygame
from tank import *
from car import *
from rocket import *
import random
import time


width_or_height = 500
screen_width = width_or_height
screen_height = width_or_height
pygame.font.init()

window = pygame.display.set_mode((screen_width, screen_height))
window.fill('light blue')

tanks = []
rockets = []
cars = []
speed = 1000
num_sprites = 5

class Game:

    def __init__(self):
        self.energy_released = 0
        # self.explosion_sound = pygame.mixer.music.load("explosion.wav")
        pygame.mixer.init()

    # Creates all sprites
    def create_sprites(self):
        for i in range(num_sprites):
            tank = Tank(self, random.randint(10, screen_width),
                        random.randint(10, screen_height), 64, i)
            tank.load()
            tanks.append(tank)

            rocket = Rocket(self, random.randint(10, screen_width),
                            random.randint(10, screen_height), 64, i)
            rocket.load()
            rockets.append(rocket)

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

            # Set up all positions
            for tank in tanks:
                tank.move()
                time.sleep(1/speed)

            for rocket in rockets:
                rocket.move()
                time.sleep(1/speed)

            for car in cars:
                car.move()
                time.sleep(1/speed)

            # Cleans the screen
            window.fill('light blue')

            # Draws all objects
            for tank in tanks:
                tank.draw()
                # print(tank.sprite_x, tank.sprite_y)
            for rocket in rockets:
                rocket.draw()

            for car in cars:
                car.draw()

            # Checks for collisions
            all_sprites = tanks + rockets + cars
            for sprite in all_sprites:
                for other_sprite in all_sprites:
                    if sprite.name != other_sprite.name:
                        if sprite.check_and_change_direction(other_sprite) == True:
                            if sprite.type == other_sprite.type:
                                if sprite.killed == False and other_sprite.killed == False:
                                    sprite.energy += 1
                                    other_sprite.energy += 1
                                    self.play_sound('../assets/punch.wav')
                                    print('Sprite Energy', sprite.energy, 'Other Sprite Energy', other_sprite.energy)
                            elif sprite.type != other_sprite.type:
                                if sprite.killed == False and other_sprite.killed == False:
                                    self.energy_released += (sprite.energy + other_sprite.energy)
                                    sprite.kill_sprite()
                                    other_sprite.kill_sprite()
                                    # pygame.mixer.music.load("explosion.wav")
                                    # pygame.mixer.music.play(loops=1)
                                    self.play_sound('../assets/explosion.wav')

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
    