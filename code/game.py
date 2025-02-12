import pygame
import pickle
from car import *
from rocket import *
from divider import *
from obstacle import *
from life import *
from stage import *
from leaderboard import *

sprite_box = 64
speed = 100000
car_move_sprite = 248
# for Nintendo Joy Cons, below are the button values.
JOYSTICK_LEFT = 1
JOYSTICK_RIGHT = 2


tanks = []
rockets = []
dividers = []
lives = []
obstacle_start_y = 50

class Game:

    def __init__(self, player_name, screen_width, screen_height):
        self.energy_released = 0

        self.name = player_name
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Init pygame
        pygame.font.init()
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.window.fill('black')
        self.obstacle1 = Obstacle(self, 0, obstacle_start_y, sprite_box, sprite_box, "Obstacle1", self.screen_width, self.screen_height) 
        self.obstacle2 = Obstacle(self, 0, obstacle_start_y, sprite_box, sprite_box, "Obstacle2", self.screen_width, self.screen_height)
        # Init sound
        pygame.mixer.init()
        self.car = None
        # self.background_image = pygame.image.load('./assets/road.jpg')
        self.background_image = pygame.transform.scale(pygame.image.load('./assets/road1.jpg'), (self.screen_width, self.screen_height))
        # initialize joy stick
        pygame.joystick.init()
        self.joyCount = pygame.joystick.get_count()
        if (self.joyCount > 0):
            # note: we only support one joystick for now
            self.joysticks = [pygame.joystick.Joystick(x) for x in range(self.joyCount)]

    # Creates all sprites
    def create_sprites(self):
        self.car = Car(self, 368, (self.screen_height-sprite_box), 1, self.screen_width, self.screen_height)

        self.life1 = Life(self, 112, 24, 64, 64, 1, self.screen_width, self.screen_height)
        self.life2 = Life(self, 112 - 44 * 1, 24, 64, 64, 2, self.screen_width, self.screen_height)
        self.life3 = Life(self, 112 - 44 * 2, 24, 64, 64, 3, self.screen_width, self.screen_height)
        lives.append(self.life1)
        lives.append(self.life2)
        lives.append(self.life3)

        
        for i in range(3):
            divider1 = Divider(self, 400, 20, 64, 64, i, self.screen_width, self.screen_height)
            divider2 = Divider(self, 400, 20, 64, 64, i, self.screen_width, self.screen_height)
            divider3 = Divider(self, 400, 20, 64, 64, i, self.screen_width, self.screen_height)
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

            if self.joyCount > 0:
                # Check for joy-stick button presses
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == JOYSTICK_RIGHT and self.car.sprite_x + car_move_sprite < self.screen_width:
                        self.car.play_sound("no_move")
                        self.car.move_x(car_move_sprite)
                    elif event.button == JOYSTICK_LEFT and self.car.sprite_x - car_move_sprite > 0:
                        self.car.play_sound("no_move")
                        self.car.move_x(-car_move_sprite)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.car.sprite_x + car_move_sprite < self.screen_width:
                        self.car.play_sound("no_move")
                        self.car.move_x(car_move_sprite)
                    elif event.key == pygame.K_LEFT  and self.car.sprite_x - car_move_sprite > 0:
                        self.car.play_sound("no_move")
                        self.car.move_x(-car_move_sprite)

            # Cleans the screen
            ## ONLY DO THIS BEFORE RENDERING ALL SPRITES
            self.window.fill('black')
            self.render_background()

            # Set up all positions
            self.car.draw()

            # Make game successively harder after each multiple of 500 in score
            if self.car.distance_travelled % 5 == 0:
                print("Increasing game speed...")
                # change reset point of the obstacle y axis
                self.obstacle1.obstacle_start_y += 5
                self.obstacle2.obstacle_start_y += 5


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
            if self.obstacle1.sprite_y == self.screen_height:
                self.obstacle1.sprite_y = self.obstacle1.obstacle_start_y + random.randint(25, 100)
                self.obstacle1.sprite_x = self.obstacle1.choose_random_x()
            else:
                self.obstacle1.sprite_y += 1

            if self.obstacle2.sprite_y == self.screen_height:
                self.obstacle2.sprite_y =self.obstacle2.obstacle_start_y + random.randint(25, 100)
                self.obstacle2.sprite_x = self.obstacle2.choose_random_x()
            else:
                self.obstacle2.sprite_y += 1


            # Draw lives
            for a_life in lives:
                if a_life.killed == False:
                    a_life.draw_heart()


            # Checks for obsctacle and car collisions
            if self.obstacle1.collided == False:
                if self.car.check_and_change_direction(self.obstacle1) == True:
                    if self.car.lives == 3:
                        self.life1.kill_sprite()
                    elif self.car.lives == 2:
                        self.life2.kill_sprite()
                        print(self.car.lives)
                    elif self.car.lives == 1:
                        self.life3.kill_sprite()
                        print(self.car.lives)
                        self.game_over()


                        return
                   
                    self.obstacle1.collided = True
                    if self.obstacle1.sprite_x == self.obstacle2.sprite_x and self.obstacle1.sprite_y == self.obstacle2.sprite_y:
                        self.obstacle2.sprite_y = self.screen_height
                    self.car.crashed()
                    self.play_sound('crash')

            if self.obstacle2.collided == False and self.obstacle1.collided == False:
                if self.car.check_and_change_direction(self.obstacle2) == True:
                    if self.car.lives == 3:
                        self.life1.kill_sprite()
                    elif self.car.lives == 2:
                        self.life2.kill_sprite()
                        print(self.car.lives)
                    elif self.car.lives == 1:
                        self.life3.kill_sprite()
                        print(self.car.lives)
                        self.game_over()
                        return
                   
                    self.obstacle2.collided = True
                    self.car.crashed()
                    self.play_sound('crash')


            # Draw obstacles randomly across dividers in X axis                        
            for divider in dividers:
                if divider.sprite_y == self.screen_height:
                    divider.sprite_y = 0



            if self.obstacle1.collided == True:
                self.obstacle1.collided = False
                self.obstacle2.obstacle_start_y = self.obstacle2.obstacle_start_y + 100
                self.obstacle1.obstacle_start_y = self.obstacle1.obstacle_start_y + 100
                self.obstacle1.sprite_y = self.obstacle1.obstacle_start_y
                self.obstacle2.sprite_y = self.obstacle2.obstacle_start_y
                self.obstacle1.sprite_x = self.obstacle1.choose_random_x()

            if self.obstacle2.collided == True:
                self.obstacle2.collided = False
                self.obstacle2.obstacle_start_y = self.obstacle2.obstacle_start_y + 100
                self.obstacle1.obstacle_start_y = self.obstacle1.obstacle_start_y + 100
                self.obstacle2.sprite_y = self.obstacle2.obstacle_start_y
                self.obstacle1.sprite_y = self.obstacle1.obstacle_start_y
                self.obstacle2.sprite_x = self.obstacle2.choose_random_x()

            # Draw text
            self.show_message(self.name.capitalize() + "\'s Score", (self.screen_width/2, 40), 30)
            self.show_message(str(round(self.car.distance_travelled)), (self.screen_width/2, 100), 80)


            # Display everything
            pygame.display.update()




    def stop(self):
        pygame.quit()
    
    
    def play_sound(self, sound_name):
        pygame.mixer.Sound('./assets/' + sound_name + '.wav').play()
    
    def stop_sound(self):
        pygame.mixer.music.stop()
    
    def show_message(self, message, spot, size):
        # sets the font and color
        font = pygame.font.SysFont('timesnewroman',  size)
        green = 0, 255, 0
        text = font.render(message, True, green)
        textRect = text.get_rect()
        # puts the score at the center of the screen
        textRect.center = (spot)
        self.window.blit(text, textRect)
        pygame.display.flip()


    def render_background(self):
        self.window.blit(self.background_image, (0, 0))


    def game_over(self):
        score = ScoreLeaderboard()
        self.the_leaderboard = score.save_score(self.name.capitalize(), self.car.distance_travelled)
        print("GAME OVER")
        self.stop_sound()
        stage = Stage()
        stage.game_over(self.window, self.car.distance_travelled, self.the_leaderboard)
