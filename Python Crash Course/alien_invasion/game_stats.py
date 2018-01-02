class GameStats:
    """a class to follow the statistics information of the game"""

    def __init__(self, ai_settings):
        """initiate statistics information"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # never reset high score
        try:
            save_file = open('save/1.sav', 'r')
        except IOError:
            self.high_score = 0
        else:
            self.high_score = float(save_file.read())

    def reset_stats(self):
        """initiate all changeable statistics information during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
