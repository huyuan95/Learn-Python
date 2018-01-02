import pygame.font
from pygame.sprite import Group

from ship import Ship


class ScoreBoard:
    """ a class to display score"""
    def __init__(self, ai_settings, screen, stats):
        """ initiate attributes about score"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # font setting for display score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(None, 48)

        # prepare score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_high_score(self):
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)
        # put high score on the  center top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = self.score_rect.top
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color,
                                            self.ai_settings.bg_color)
        # put score on right top corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        rounded_level = int(round(self.stats.level, -1))
        level_str = "{:,}".format(rounded_level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color,
                                            self.ai_settings.bg_color)
        # put score on right top corner
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = self.high_score_rect.bottom + 10
        self.level_rect.centerx = self.score_rect.centerx

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
