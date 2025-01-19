import pygame
import sys
from controls.textinputbox import TextInputBox

class GameStart:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        pygame.display.set_caption("F1 Racing Stimulator")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
        self.background_image = pygame.transform.scale(pygame.image.load('./assets/road1.jpg'), (screen_width, screen_height))
        self.screen.blit(self.background_image, (0, 0))

    def get_user_name(self):
        input_box_width = self.screen_width * 0.7
        input_box_height = 40
        input_box_x = (self.screen_width - input_box_width) / 2
        input_box_y = (self.screen_height - input_box_height) / 2
        white_color = (255, 255, 255)

        # Draw label
        label_surface = pygame.font.Font(None, input_box_height).render("Enter your name:", True, white_color)
        self.screen.blit(label_surface, (input_box_x, input_box_y-label_surface.get_height()-5))

        # Draw input box
        input_box = TextInputBox(self.screen, input_box_x, input_box_y, input_box_width, input_box_height)
        input_box.draw()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.USEREVENT and event.action == 'quit':
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.USEREVENT and event.action == 'enter':
                    return event.text