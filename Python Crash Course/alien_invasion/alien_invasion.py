import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button


def run_game():
    # initiate the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # create a "Play" button
    play_button = Button(ai_settings, screen, 'Play')
    # create an instance to store statistics information of the game and
    # create score board
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group to store the bullets
    bullets = Group()
    # create a group to store the aliens
    aliens = Group()
    # create aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:

        # monitor keyboard and mouse event
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
