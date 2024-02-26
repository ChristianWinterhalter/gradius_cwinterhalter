# import math
# import sys
# from time import sleep
#
# import pygame
#
# from settings import Settings
# from game_stats import GameStats
# from scoreboard import Scoreboard
# from button import Button
# from bullet import Bullet
# from ship import Ship
# from alien import Alien
#
#
# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""
#
#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.settings = Settings()
#         self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
#         pygame.mixer.music.load("assets/ost/Space Harrier Music - MAIN THEME.mp3")
#         pygame.mixer.music.set_volume(0.05)
#         pygame.mixer.music.play()
#         pygame.display.set_caption("Alien Invasion")
#
#         # Create instance of game statistics
#         self.stats = GameStats(self)
#         self.scoreboard = Scoreboard(self)
#
#         # Load background image
#         self.bg = pygame.image.load("assets/images/background/EmptyStarfield.jpg").convert()
#         self.bg_width = self.bg.get_width()
#         # bg image is larger than screen so we divide the bg width by the screen width
#         # if the opposite was true we would divide the screen width by the bg width.
#         self.bg_tiles = math.ceil(self.bg_width / self.settings.screen_width)
#         self.scroll = 0
#
#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()
#
#         self._create_fleet()
#
#         # Create Play button
#         self.play_button = Button(self, "Play")
#
#         # Create Quit button
#         self.quit_button = Button(self, "Quit", [0, 100])
#
#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events.
#             self._check_events()
#
#             # Update ship & bullet sprite group
#             if self.stats.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()
#                 self._check_bullet_alien_collisions()
#
#                 # Redraw the screen during each pass through the loop.
#             self._update_screen()
#
#     def _check_events(self):
#         """Respond to key-presses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)
#                 self._check_quit_button(mouse_pos)
#
#     def _check_play_button(self, mouse_pos):
#         button_text = "reset"
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         """Start a new game when the player clicks Play."""
#         if button_clicked and not self.stats.game_active:
#             # Reset the game statistics
#             self.stats.reset_stats()
#             self.stats.game_active = True
#
#             # Get rid of any remaining aliens and bullets.
#             self.aliens.empty()
#             self.bullets.empty()
#
#             # Create a new fleet and center the ship.
#             self._create_fleet()
#             self.ship.reset_ship()
#
#             # Update Play button to Reset
#             self.play_button.prep_msg("Reset")
#
#             # Hide the mouse cursor.
#             pygame.mouse.set_visible(False)
#
#     def _check_quit_button(self, mouse_pos):
#         button_clicked = self.quit_button.rect.collidepoint(mouse_pos)
#         """Quit the game when the player clicks Quit button"""
#         if button_clicked and not self.stats.game_active:
#             sys.exit()
#
#     def _check_keydown_events(self, event):
#         """ Respond to keydown presses."""
#         if event.key == pygame.K_d:
#             # Move the ship to the right.
#             self.ship.moving_right = True
#         elif event.key == pygame.K_a:
#             # Move the ship to the left.
#             self.ship.moving_left = True
#         elif event.key == pygame.K_w:
#             # Move the ship to the up.
#             self.ship.moving_up = True
#         elif event.key == pygame.K_s:
#             # Move the ship to the down.
#             self.ship.moving_down = True
#         elif event.key == pygame.K_SPACE:
#             # Fire a bullet
#             self._fire_bullet()
#         elif event.key == pygame.K_t:
#             # DEBUG spawn an alien
#             self._create_fleet()
#         elif event.key == pygame.K_q:
#             # Flip boolean game_active, this functions as a Pause button.
#             self.stats.game_active = not self.stats.game_active
#             self.play_button.draw_button()
#             self.quit_button.draw_button()
#             pygame.mouse.set_visible(not self.stats.game_active)
#
#     def _check_keyup_events(self, event):
#         """Respond to keyup releases."""
#         if event.key == pygame.K_d:
#             # Move the ship to the right.
#             self.ship.moving_right = False
#         elif event.key == pygame.K_a:
#             # Move the ship to the left.
#             self.ship.moving_left = False
#         elif event.key == pygame.K_w:
#             # Move the ship to the up.
#             self.ship.moving_up = False
#         elif event.key == pygame.K_s:
#             # Move the ship to the down.
#             self.ship.moving_down = False
#
#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#
#         # Decrement ships_left.
#         self.stats.lives_left -= 1
#         self._reset_game()
#
#         if self.stats.lives_left > 0:
#             # Reset the game state
#             self._reset_game()
#         else:
#             # End the Game
#             self.stats.game_active = False
#
#             # Update Reset button to Play
#             self.play_button.prep_msg("Play")
#
#             # Re-enable mouse pointer
#             pygame.mouse.set_visible(True)
#
#     def _reset_game(self):
#         # Clean up game
#         self.aliens.empty()
#         self.bullets.empty()
#
#         # Reset game
#         self.ship.reset_ship()
#         self._create_fleet()
#
#         # Pause for player recognition of game state.
#         sleep(0.5)
#
#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()
#
#         # Get rid of bullets that are off-screen.
#         for bullet in self.bullets.copy():
#             if bullet.rect.right >= self.settings.screen_width:
#                 self.bullets.remove(bullet)
#
#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Check for any bullets that have hit aliens.
#         # If so, get rid of said bullets and aliens.
#         collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
#                                                 True, True)
#
#     def _update_aliens(self):
#         """
#         Check if the fleet is at an edge, then update
#         the positions of all aliens in a fleet.
#         """
#         self._check_fleet_edges()
#         self.aliens.update()
#
#         for alien in self.aliens.copy():
#             if alien.rect.left < -50:
#                 self.aliens.remove(alien)
#
#         # Look for alien-ship collisions, scale the collision rect by .75.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens, pygame.sprite.collide_rect_ratio(0.75)):
#             print("Ship Hit!")
#             self._ship_hit()
#             print(self.stats.lives_left)
#
#         # Check if there are no more aliens in SpriteGroup(Aliens)
#         if not self.aliens:
#             # Increase game difficulty and loop through fleet creation
#             self.stats.difficulty += 1
#             offset_x = 50
#             # Create new alien fleets based on difficulty.
#             for i in range(0, self.stats.difficulty):
#                 self._create_fleet(offset_x * i)
#
#             self.settings.increase_speed()
#
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         # for i in range(0, self.bg_tiles):
#         #     self.screen.blit(self.bg, (self.bg_width / i + self.scroll, 0))
#         #
#         # # scroll background
#         # self.scroll -= 5
#         self.screen.blit(self.bg, (0, 0))
#
#         # reset scroll
#         if abs(self.scroll) > self.bg_width:
#             scroll = 0
#
#         self.ship.blitme()
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#
#         for alien in self.aliens.sprites():
#             alien.draw_alien()
#
#         # Draw the score information.
#         self.scoreboard.show_score()
#
#         # Draw the play button if the game is inactive.
#         if not self.stats.game_active:
#             self.play_button.draw_button()
#             self.quit_button.draw_button()
#
#         # Make the most recently drawn screen visible.
#         pygame.display.flip()
#
#     def _fire_bullet(self):
#         """ Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)
#
#     def _create_fleet(self, offset_x=0):
#         """Create a fleet of aliens."""
#         alien = Alien(self, offset_x=offset_x)
#         alien_height = alien.rect.height
#         alien_spacing = 2 * alien_height
#         available_space_y = self.settings.screen_height - alien_spacing
#         # available_space_x = settings.screen_width - (3 * alien_width) - alien_width
#         number_aliens_y = available_space_y // alien_spacing
#
#         # Create the first row of aliens
#         for alien_number in range(number_aliens_y):
#             # Create an alien and place it in the row.
#             alien = Alien(self)
#             alien.y = alien_height + alien_spacing * alien_number
#             alien.rect.y = alien.y
#             self.aliens.add(alien)
#
#     def _check_fleet_edges(self):
#         """Respond appropriately if any aliens have reached an edge."""
#         for alien in self.aliens.sprites():
#             alien.check_edges()
#
#
# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()
