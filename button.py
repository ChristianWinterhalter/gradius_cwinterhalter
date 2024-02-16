import pygame.font


class Button:

    def __init__(self, ai_game, msg, rect_offset=[0, 0]):
        """Initialize button attributes."""
        self.msg_image_rect = None
        self.msg_image = None
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = tuple(map(sum, zip(self.screen_rect.center, rect_offset)))

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg, rect_offset=None):
        """Turn msg into a rendered image and center text on the button."""
        if rect_offset is None:
            rect_offset = [0, 0]

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        # self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.center = tuple(map(sum, zip(self.rect.center, rect_offset)))

    def draw_button(self):
        # Draw blank button and then draw our message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
