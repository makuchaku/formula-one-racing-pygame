import pygame
import sys
import pygame_gui

class GameStart:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        pygame.display.set_caption("Your game starts here...")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
        self.background_image = pygame.transform.scale(pygame.image.load('./assets/road.jpg'), (screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.ui_manager = pygame_gui.UIManager((screen_width, screen_height))
        self.create_text_input()

    def create_text_input(self):   
        text_input_width = 500
        text_input_height = 50
        text_input_x = int((self.screen_width - text_input_width)/2)
        text_input_y = (self.screen_height/2) - text_input_height
        self.text_input = pygame_gui.elements.UITextEntryLine(
            relative_rect = pygame.Rect((text_input_x, text_input_y), (text_input_width, text_input_height)),
            manager = self.ui_manager,
            object_id = "#main_text_entry",
            placeholder_text = "Write your name here and press Enter!")
        self.text_input.set_text_length_limit(50)
                                                                              
    def get_user_name(self):
        while True:
            ui_refresh_rate = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.text_input.focus()

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit

                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry"):
                    if event.text.strip() == "":
                        self.text_input.unfocus()
                    else:
                        return event.text

                self.ui_manager.process_events(event)

            self.ui_manager.update(ui_refresh_rate)
            self.screen.blit(self.background_image, (0, 0))
            self.ui_manager.draw_ui(self.screen)
            pygame.display.update()

