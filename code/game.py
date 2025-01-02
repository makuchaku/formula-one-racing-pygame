import pygame
from car import Car
from rocket import Rocket
from divider import Divider
from obstacle import Obstacle
from life import Life

SPRITE_BOX = 64
SPEED = 100000
CAR_MOVE_SPRITE = 248

# Replaces global lists with class-level tracking if desired
tanks = []
rockets = []
dividers = []
lives = []

OBSTACLE_START_Y = 10


class Game:
    """
    Manages the core loop and rendering logic of the car-and-obstacle game.

    Attributes:
        name (str):        The player's name, used for UI display.
        screen_width (int):  The game window width in pixels.
        screen_height (int): The game window height in pixels.
        energy_released (int): Additional placeholder or scoring mechanic.
        car (Car):         The player's car object.
        obstacle1 (Obstacle): The first dynamic obstacle.
        obstacle2 (Obstacle): The second dynamic obstacle.
        background_image (Surface): The loaded background image.
        window (Surface):  The main PyGame display surface.
    """

    def __init__(self, player_name, screen_width, screen_height):
        """
        Initializes the game environment and window.

        Args:
            player_name:    The player's in-game name for display.
            screen_width:   The width of the game window in pixels.
            screen_height:  The height of the game window in pixels.
        """
        self.energy_released = 0
        self.name = player_name
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize PyGame and set up the screen
        pygame.font.init()
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.window.fill('black')

        # Prepare obstacles
        self.obstacle1 = Obstacle(self, 0, OBSTACLE_START_Y, SPRITE_BOX,
                                  "Obstacle1", self.screen_width, self.screen_height)
        self.obstacle2 = Obstacle(self, 0, OBSTACLE_START_Y, SPRITE_BOX,
                                  "Obstacle2", self.screen_width, self.screen_height)

        # Sound initialization
        pygame.mixer.init()

        self.car = None  # Will be created in create_sprites
        # Load and scale background
        raw_bg = pygame.image.load('./assets/road.jpg')
        self.background_image = pygame.transform.scale(raw_bg, (self.screen_width, self.screen_height))

    def create_sprites(self):
        """
        Creates and positions the initial sprites:
         - The player's car
         - Lives (heart icons)
         - Dividers for the road
        """
        # Car is centered horizontally, near the bottom
        x_pos = (self.screen_width - SPRITE_BOX) / 2
        y_pos = self.screen_height - SPRITE_BOX
        self.car = Car(self, x_pos, y_pos, SPRITE_BOX, 1, self.screen_width, self.screen_height)

        # Create life hearts
        # The first life is at (112, 24), each subsequent heart offset by 44 pixels
        life1 = Life(self, 112, 24, 64, 1, self.screen_width, self.screen_height)
        life2 = Life(self, 112 - 44, 24, 64, 2, self.screen_width, self.screen_height)
        life3 = Life(self, 112 - 88, 24, 64, 3, self.screen_width, self.screen_height)
        lives.extend([life1, life2, life3])

        # Create road dividers
        for i in range(3):
            divider1 = Divider(self, 400, 20, 64, i, self.screen_width, self.screen_height)
            divider2 = Divider(self, 400, 20, 64, i, self.screen_width, self.screen_height)
            divider3 = Divider(self, 400, 20, 64, i, self.screen_width, self.screen_height)

            # Distinguish the sprite_x offset for visual variety
            if i == 0:
                divider1.draw_divider(1 * 248, 20)
                divider2.draw_divider(1 * 248, 300)
                divider3.draw_divider(1 * 248, 600)
            else:
                divider1.draw_divider(2 * 248, 20)
                divider2.draw_divider(2 * 248, 300)
                divider3.draw_divider(2 * 248, 600)

            dividers.extend([divider1, divider2, divider3])

    def render_frames(self):
        """
        The main game loop, responsible for:
         - Polling events (keyboard, etc.)
         - Moving, drawing, and collision-checking sprites
         - Updating the display
        """
        while True:
            event = pygame.event.poll()

            # Handle exit
            if event.type == pygame.QUIT:
                break

            # Handle keyboard events for car movement
            elif event.type == pygame.KEYDOWN:
                self.handle_car_movement(event.key)

            # Clear screen and draw background
            self.window.fill('black')
            self.render_background()

            # Draw the player's car
            self.car.draw()

            # Move and draw obstacles
            self.handle_obstacles()

            # Move road dividers, increase distance traveled
            for divider in dividers:
                divider.move_y(1)
                if self.car.lives > 0:
                    self.car.distance_travelled = round(self.car.distance_travelled + 0.01, 2)

            for divider in dividers:
                divider.draw_divider(divider.sprite_x, divider.sprite_y)

            # Draw hearts
            for a_life in lives:
                if not a_life.killed:
                    a_life.draw_heart()

            # Check collisions with obstacles
            self.check_collision_with_obstacle(self.obstacle1)
            self.check_collision_with_obstacle(self.obstacle2)

            # Redraw text (score, etc.)
            self.show_message(f"{self.name.capitalize()}'s Score", (self.screen_width / 2, 40), 30)
            self.show_message(str(round(self.car.distance_travelled)), (self.screen_width / 2, 100), 80)

            # Update display
            pygame.display.update()

    def handle_car_movement(self, key):
        """
        Parses key presses for left/right movement, ensuring the car doesn't go out of bounds.
        """
        # Right boundary at x=616, left boundary at x=120
        if key == pygame.K_RIGHT:
            if self.car.sprite_x < 616:
                self.car.play_sound("no_move")
                self.car.move_x(CAR_MOVE_SPRITE)
        elif key == pygame.K_LEFT:
            if self.car.sprite_x > 120:
                self.car.play_sound("no_move")
                self.car.move_x(-CAR_MOVE_SPRITE)

    def handle_obstacles(self):
        """
        Moves obstacles and resets their positions when they reach the screen bottom.
        """
        # Draw and move obstacle1
        self.obstacle1.draw()
        if self.obstacle1.sprite_y == self.screen_height:
            self.obstacle1.sprite_y = OBSTACLE_START_Y
        else:
            self.obstacle1.sprite_y += 1

        # Draw and move obstacle2
        self.obstacle2.draw()
        if self.obstacle2.sprite_y == self.screen_height:
            self.obstacle2.sprite_y = OBSTACLE_START_Y
        else:
            self.obstacle2.sprite_y += 1

        # Reset them if they pass the bottom edge
        if self.obstacle1.sprite_y == self.screen_height:
            self.obstacle1.collided = False
            self.obstacle1.sprite_x = self.obstacle1.choose_random_x()

        if self.obstacle2.sprite_y == self.screen_height:
            self.obstacle2.collided = False
            self.obstacle2.sprite_x = self.obstacle2.choose_random_x()

    def check_collision_with_obstacle(self, obstacle):
        """
        Checks collision between the car and a given obstacle.
        Reduces car life if collision occurs.
        """
        if not obstacle.collided:
            collided = self.car.check_and_change_direction(obstacle)
            if collided:
                obstacle.collided = True
                # Move obstacle off-screen
                obstacle.sprite_y += self.screen_height
                self.play_sound('crash')
                self.handle_life_loss()

    def handle_life_loss(self):
        """
        Reduces the car's life by one and kills the corresponding heart sprite.
        If life drops to zero, triggers game over.
        """
        if self.car.lives == 3:
            lives[0].kill_sprite()
            self.car.lives = 2
        elif self.car.lives == 2:
            lives[1].kill_sprite()
            self.car.lives = 1
        elif self.car.lives == 1:
            lives[2].kill_sprite()
            self.car.lives = 0
            self.game_over()

    def stop(self):
        """
        Safely quits the pygame context and closes the window.
        """
        pygame.quit()

    def play_sound(self, sound_name):
        """
        Plays a .wav file from the assets folder by name (excluding extension).
        """
        try:
            sound_path = f'./assets/{sound_name}.wav'
            sound = pygame.mixer.Sound(sound_path)
            sound.play()
        except pygame.error as e:
            print(f"Sound error: {e}")

    def show_message(self, message, position, font_size):
        """
        Renders a message at the given screen position with the specified font size.
        """
        font = pygame.font.SysFont('timesnewroman', font_size)
        color = (0, 0, 0)  # black text
        text_surf = font.render(message, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = position
        self.window.blit(text_surf, text_rect)
        pygame.display.flip()

    def render_background(self):
        """
        Blits the preloaded road background onto the main window at (0,0).
        """
        self.window.blit(self.background_image, (0, 0))

    def game_over(self):
        """
        Prints "GAME OVER" in the console and could trigger end-of-game logic.
        """
        print("GAME OVER")
