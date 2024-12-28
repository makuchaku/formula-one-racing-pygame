
class Sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_x, sprite_y, width, sprite_position, name, type, energy):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.texture = pygame.image.load('sprites.png')
        self.rect = pygame.Rect(width, sprite_position * width, width, width)
        self.direction_x = 1
        self.direction_y = 1
        self.width = width
        self.name = name
        self.type = type
        self.energy = 1
        self.killed = False


    def load(self):
        self.draw()

    def draw(self):
        location = pygame.math.Vector2(self.sprite_x, self.sprite_y)
        if self.killed == False:
            # pygame.draw.rect(window, (255,0,0), [0, 0, self.width, self.width], 1)
            window.blit(self.texture, location, self.rect)

    # Move on x axis primitive
    def move_x(self, move_x):
        self.sprite_x += move_x

    # Move on y axis primitive
    def move_y(self, move_y):
        self.sprite_y += move_y

    def move(self):
        if self.killed == True:
            return
        # X
        if self.sprite_x == 0:
            self.direction_x = 1
        if self.sprite_x == screen_width - self.width:
            game.play_sound('punch.wav')
            self.direction_x = -1
            # Sometimes, change the y direction
            if (random.randint(0, 1000) % 2 == 0):
                self.direction_y = -1

        # add in the direction randomly
        if (random.randint(0, 1000) % 2 == 0):
            self.move_x(1 * self.direction_x)

        # Y
        if self.sprite_y == 0:
            self.direction_y = 1
        if self.sprite_y == screen_height - self.width:
            game.play_sound('punch.wav')
            self.direction_y = -1
            # Sometimes, change the x direction
            if (random.randint(0, 1000) % 2 == 0):
                self.direction_x = -1

        # add in the direction randomly
        if (random.randint(0, 1000) % 3 == 0):
            self.move_y(1 * self.direction_y)


    def check_collision(self, other_sprite):
        if (self.sprite_x < other_sprite.sprite_x + other_sprite.width and
            self.sprite_x + self.width > other_sprite.sprite_x and
            self.sprite_y < other_sprite.sprite_y + other_sprite.width and
            self.sprite_y + self.width > other_sprite.sprite_y):
            print('COLLISION DETECTED BETWEEN', self.name, other_sprite.name)
            return True
        return False
    
    
    def __check_collision(self, other_sprite):
        x = self.sprite_x
        y = self.sprite_y
        _x = other_sprite.sprite_x
        _y = other_sprite.sprite_y
        if(
            # x is between _x and _x + width
            (x >= _x and x <= _x + other_sprite.width)
            # y is between _y and _y + height
            or (y >= _y and y <= _y + other_sprite.width)
          ):
            return True
        
        return False
    

    def check_and_change_direction(self, other_sprite):
        if self.check_collision(other_sprite) == True:
            if self.direction_x == -1 and self.direction_y == -1:
                self.direction_x = 1
                self.direction_y = 1
            elif self.direction_x == 1 and self.direction_y == 1:
                self.direction_x = -1
                self.direction_y = -1
            elif self.direction_x == -1 and self.direction_y == 1:
                self.direction_x = 1
                self.direction_y = -1
            elif self.direction_x == 1 and self.direction_y == -1:
                self.direction_x = -1
                self.direction_y = 1
            return True
        return False

    def kill_sprite(self):
        self.killed = True