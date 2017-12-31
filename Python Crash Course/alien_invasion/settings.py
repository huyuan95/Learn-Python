class Settings:
    """ Class to store all settings for alien_invasion."""

    def __init__(self):
        """Initiate the settings of the game."""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50

        # fleet direction: 1 = right, -1 = left
        self.fleet_direction = 1
