import pygame
from car import *
from rocket import *
from divider import *
from obstacle import *
from life import *

screen_width = 800
screen_height = 600

sprite_box = 64
speed = 100000
car_move_sprite = 248


tanks = []
rockets = []
dividers = []
lives = []
obstacle_start_y = 10


class Game:

    def __init__(self):
        self.energy_released = 0

        # Init pygame
        pygame.font.init()
        window = pygame.display.set_mode((screen_width, screen_height))
        window.fill('black')
        self.obstacle1 = Obstacle(self, 0, obstacle_start_y, sprite_box, "Obstacle1") 
        self.obstacle2 = Obstacle(self, 0, obstacle_start_y, sprite_box, "Obstacle2")
        # Init sound
        pygame.mixer.init()
        self.car = None
        # self.background_image = pygame.image.load('./assets/road.jpg')
        self.background_image = pygame.transform.scale(pygame.image.load('./assets/road.jpg'), (screen_width, screen_height))


 
    # Creates all sprites
    def create_sprites(self):
        self.car = Car(self, (screen_width-sprite_box)/2, (screen_height-sprite_box), sprite_box, 1)

        self.life1 = Life(self, 112, 24, 64, 1)
        self.life2 = Life(self, 112 - 44 * 1, 24, 64, 2)
        self.life3 = Life(self, 112 - 44 * 2, 24, 64, 3)
        lives.append(self.life1)
        lives.append(self.life2)
        lives.append(self.life3)

        
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

         


    # Each iteration is a frame
    def render_frames(self):
        while True:
            event = pygame.event.poll()
            # Check if we need to quit
            if event.type == pygame.QUIT:
                break

            # Check for movement
            elif event.type == pygame.KEYDOWN:
                if self.car.sprite_x == 616 and event.key == pygame.K_RIGHT:
                    # self.car.play_sound("move")
                    # Don't move, already at right boundary
                    pass
                elif self.car.sprite_x == 120 and event.key == pygame.K_LEFT:
                    # self.car.play_sound("move")
                    # Don't move, already at left boundary
                    pass
                elif event.key == pygame.K_RIGHT and self.car.sprite_x != 616:
                    self.car.play_sound("no_move")
                    self.car.move_x(car_move_sprite)
                elif event.key == pygame.K_LEFT and self.car.sprite_x != 120:
                    self.car.play_sound("no_move")
                    self.car.move_x(-car_move_sprite)



            # Cleans the screen
            ## ONLY DO THIS BEFORE RENDERING ALL SPRITES
            window.fill('black')
            self.render_background()

            # Set up all positions
            self.car.draw()

            # Draw obstacles
            self.obstacle1.draw()
            self.obstacle2.draw()


            # Render dividers
            for divider in dividers:
                divider.move_y(1)
                if not self.car.lives == 0:
                    self.car.distance_travelled = round(self.car.distance_travelled + 1/100, 2)

            for divider in dividers:
                divider.draw_divider(divider.sprite_x, divider.sprite_y)

            # If obstacle hits the bottom of screen, start it from the top again
            if self.obstacle1.sprite_y == screen_height:
                self.obstacle1.sprite_y = obstacle_start_y
            else:
                self.obstacle1.sprite_y += 1

            if self.obstacle2.sprite_y == screen_height:
                self.obstacle2.sprite_y = obstacle_start_y
            else:
                self.obstacle2.sprite_y += 1


            # Draw lives
            for a_life in lives:
                if a_life.killed == False:
                    a_life.draw_heart()


            # Checks for obsctacle and car collisions
            if self.obstacle1.collided == False:
                if self.car.check_and_change_direction(self.obstacle1) == True:
                    # print('car collided with obstacle1')
                    if self.car.lives == 3:
                        self.life1.kill_sprite()
                        self.car.lives = 2
                        self.obstacle1.sprite_y += screen_height
                        self.play_sound('crash')
                        self.obstacle1.collided == True

                    elif self.car.lives == 2:
                        self.life2.kill_sprite()
                        self.car.lives = 1
                        self.obstacle1.sprite_y += screen_height
                        self.play_sound('crash')
                        self.obstacle1.collided == True
                        print(self.car.lives)

                    elif self.car.lives == 1:
                        self.life3.kill_sprite()
                        self.car.lives  = 0
                        self.obstacle1.sprite_y += screen_height
                        self.play_sound('crash')
                        self.obstacle1.collided == True
                        print(self.car.lives)




            
            elif self.obstacle2.collided == False:
                if self.car.check_and_change_direction(self.obstacle2) == True:
                    # print('car collided with obstacle2')
                    if self.car.lives == 3:
                        self.life1.kill_sprite()
                        self.car.lives = 2
                        self.obstacle2.sprite_y += screen_height
                        self.play_sound('crash')
                        self.obstacle2.collided == True

                    elif self.car.lives == 2:
                        self.life2.kill_sprite()
                        self.car.lives = 1
                        self.obstacle2.sprite_y += screen_height
                        self.play_sound('crash')
                        self.obstacle2.collided == True
                        print(self.car.lives)

                    elif self.car.lives == 1:
                        self.life3.kill_sprite()
                        self.car.lives  = 0
                        self.obstacle2.sprite_y += screen_height
                        self.play_sound('crash')
                        self.obstacle2.collided == True
                        print(self.car.lives)





            # Draw obstacles randomly across dividers in X axis                        
            for divider in dividers:
                if divider.sprite_y == screen_height:
                    divider.sprite_y = 0

            if self.obstacle1.sprite_y == screen_height:
                self.obstacle1.collided = False
                self.obstacle1.sprite_y = obstacle_start_y
                self.obstacle1.sprite_x = self.obstacle1.choose_random_x()

            if self.obstacle2.sprite_y == screen_height:
                self.obstacle2.collided = False
                self.obstacle1.sprite_y = obstacle_start_y
                self.obstacle2.sprite_x = self.obstacle2.choose_random_x()

            # Draw text
            self.show_message(str(round(self.car.distance_travelled)), (screen_width/2, 50))


            # Display everything
            pygame.display.update()




    def stop(self):
        pygame.quit()
    
    
    def play_sound(self, sound_name):
        pygame.mixer.Sound('./assets/' + sound_name + '.wav').play()

    
    def show_message(self, message, spot):
        # sets the font and color
        font = pygame.font.SysFont('timesnewroman',  80)
        green = 0, 0, 0
        text = font.render(message, True, green)
        textRect = text.get_rect()
        # puts the score at the center of the screen
        textRect.center = (spot)
        window.blit(text, textRect)
        pygame.display.flip()


    def render_background(self):
        window.blit(self.background_image, (0, 0))