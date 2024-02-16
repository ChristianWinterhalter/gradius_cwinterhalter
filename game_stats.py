class GameStats:
    """Track statistics for Alien invasion game."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.ai_settings = ai_game.settings
        self.score = 0
        # Start Alien Invasion in an active state.
        self.game_active = False
        self.lives_left = self.ai_settings.player_stocks
        self.difficulty = 0
        self.reset_stats()

    def reset_stats(self):
        """Re-initialize statistics that can change during the game."""
        self.lives_left = self.ai_settings.player_stocks
        self.score = 0
        self.difficulty = 0