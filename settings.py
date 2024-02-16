import pygame


class Settings:
    """A class to store all settings for Alien Invasion Game"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 70, 70)

        # Ship collider
        self.ship_collider = pygame.rect.Rect(0, 0, 20, 10)

        # Ship settings
        self.ship_rect_size = pygame.rect.Rect(0, 0, 26, 16)
        self.ship_scale_transform = (88, 40)
        self.player_stocks = 3
        self.ship_speed = 0.4

        # Bullet settings
        self.bullet_speed = 0.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 0, 150)
        self.bullets_allowed = 23

        # Metroid Alien Sprites
        self.metroid_alien_speed = 0.1
        self.metroid_alien_drop_speed = 120
        # fleet direction of 1 represents down; -1 represents up.
        self.metroid_alien_fleet_direction = 1
        self.metroid_rect_size = pygame.rect.Rect(0, 0, 26, 23)
        self.metroid_scale_transform = (72, 48)

        # Increase game speed + difficulty
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 0.4
        self.bullet_speed = 0.6
        self.metroid_alien_speed = 0.1

        # fleet direction of 1 represents down; -1 represents up.
        self.metroid_alien_fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.metroid_alien_speed *= self.speedup_scale
