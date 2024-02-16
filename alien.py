import pygame
from spritesheet import Spritesheet
from spritestripanim import SpriteStripAnim
from pygame.sprite import Sprite


class Alien(Sprite):
    """Enemy Alien class"""

    def __init__(self, ai_game, alien_speed=0.2, direction=-1, offset_x=0):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('assets/images/sprites/enemy/Metroid.bmp')
        self.transColor = self.image.get_at((0, 0))

        # Load the alien image and get its rect.
        self.spriteAnim = SpriteStripAnim('assets/images/sprites/enemy/Metroid.bmp', self.settings.metroid_rect_size,
                                          2, colorkey=self.transColor, loop=True, frames=200)
        self.image = pygame.transform.scale(self.spriteAnim.current(), self.settings.metroid_scale_transform)

        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright

        self.x = float(self.rect.x - offset_x)
        self.y = float(self.rect.y)
        self.rect.x = self.x

        self.speed = alien_speed
        self.direction = direction

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            self.direction *= -1
            self.rect.x -= self.settings.metroid_alien_drop_speed
            return True
        else:
            return False

    def update(self, *args, **kwargs):
        self.x -= float(self.speed / 2)
        self.y += float(self.speed * self.direction * 3)
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = pygame.transform.scale(self.spriteAnim.next(), self.settings.metroid_scale_transform)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
