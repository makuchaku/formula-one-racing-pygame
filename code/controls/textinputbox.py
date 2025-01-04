import pygame

Darak_Gray_Color = (59, 59, 59)
Gray_Color = (200, 200, 200)
cursor_padding = 10

class TextInputBox:
    def __init__(self, parent_screen, x, y, width, height, text="", background_color=Gray_Color, text_color=Darak_Gray_Color):
        self.parent_screen = parent_screen
        self.height = height
        self.text = text
        self.background_color = background_color
        self.font = pygame.font.Font(None, height - cursor_padding)
        self.text_color = text_color
        self.input_box = pygame.Rect(x, y, width, height)

    def draw(self):
        cursor_pos = len(self.text)
        cursor_visible = True
        cursor_timer = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'action': 'quit'}))
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if len(self.text.strip()) == 0:
                            continue
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'action': 'enter', 'text': self.text.strip()}))
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        if cursor_pos > 0:
                            self.text = self.text[:cursor_pos - 1] + self.text[cursor_pos:]
                            cursor_pos -= 1
                    elif event.key == pygame.K_DELETE:
                        if cursor_pos < len(self.text):
                            self.text = self.text[:cursor_pos] + self.text[cursor_pos+1:]
                    elif event.key == pygame.K_LEFT:
                        if cursor_pos > 0:
                            cursor_pos -= 1
                    elif event.key == pygame.K_RIGHT:
                        if cursor_pos < len(self.text):
                            cursor_pos += 1
                    else:
                        self.text = self.text[:cursor_pos] + event.unicode + self.text[cursor_pos:]
                        cursor_pos += 1

            # Draw input box and text
            pygame.draw.rect(self.parent_screen, self.background_color, self.input_box)
            text_surface = self.font.render(self.text, True, self.text_color)
            self.parent_screen.blit(text_surface, (self.input_box.x + cursor_padding, self.input_box.y + cursor_padding))

            # Toggle cursor visibility
            if pygame.time.get_ticks() - cursor_timer > 500:
                cursor_visible = not cursor_visible
                cursor_timer = pygame.time.get_ticks()

            # Draw cursor
            if cursor_visible:
                cursor_x = self.input_box.x + cursor_padding + self.font.size(self.text[:cursor_pos])[0]
                cursor_y = self.input_box.y + cursor_padding
                cursor_height = self.input_box.y + self.height-cursor_padding
                pygame.draw.line(self.parent_screen, self.text_color, (cursor_x, cursor_y), (cursor_x, cursor_height), 2)

            pygame.display.flip()