class GameStats():
    '''a class to follow the statistics infomation of the game'''

    def __init__(self, ai_settings):
        '''intiate statistics information'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        '''initiate all changable statistics information during the game'''
        self.ships_left = self.ai_settings.ship_limit
