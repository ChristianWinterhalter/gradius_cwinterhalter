import pygame
from spritestripanim import SpriteStripAnim


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('assets/images/sprites/player/ship/viper_spriteanim.bmp')
        self.transColor = self.image.get_at((0, 0))

        # Load the ship image and get its rect.
        self.spriteAnim = SpriteStripAnim('assets/images/sprites/player/ship/viper_spriteanim.bmp',
                                          self.settings.ship_rect_size, 9, colorkey=self.transColor,
                                          loop=False,
                                          frames=200, start_frame=4)
        self.image = pygame.transform.scale(self.spriteAnim.current(),
                                            self.settings.ship_scale_transform)

        # Start each new ship at the bottom center of the screen.
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        updated_sprite = False

        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            self.image = pygame.transform.scale(self.spriteAnim.previous(), self.settings.ship_scale_transform)
            updated_sprite = True

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            self.image = pygame.transform.scale(self.spriteAnim.next(), self.settings.ship_scale_transform)
            updated_sprite = True

        #if not updated_sprite:
        #     if self.spriteAnim.f != self.spriteAnim.frames
        # Update rect object from x and y variable
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def reset_ship(self):
        """Reset to start position."""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

