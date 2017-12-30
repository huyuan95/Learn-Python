import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''respond for keydown event'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a bullet and add it to bullets group
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''respond for keyup event'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    #respond for events of keyboard or mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets, play_button):
    '''Update the image on screen and turn to new screen'''
    #redraw the screen in every iteration
    screen.fill(ai_settings.bg_color)
    #redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #if game is not active, draw Play button
    play_button.draw_button()

    #make recent drawing screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''update bullet position and delete disapeared bullet'''
    #update bullet position
    bullets.update()

    #delete disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens,bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    '''respond for the collision of bullets and aliens'''
    # delete the collision bullet and alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #delete all bullets and create a new group of aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    '''calculate capacity in a row'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #create a alien and put it in the current row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    '''calculate column capacity in the screen'''
    available_space_y = (ai_settings.screen_height - (3*alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):
    '''Create aliens'''
    #create a alien, calculate capacity in a row
    #space between the aliens is the alien width
    alien=Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_alien_y = get_number_rows(ai_settings, ship.rect.height,
                                     alien.rect.height)

    #create first row aliens
    for row_number in range(number_alien_y):
        for alien_number in range(number_alien_x):
            #create a alien and add to this row
            create_alien(ai_settings, screen, aliens, alien_number,row_number)

def check_fleet_edges(ai_settings, aliens):
    '''take corresponding issue when alien reach screen edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''move all aliens downward, change their direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''respond for the ship collided with alien'''
    if stats.ships_left > 0:
        # decrease ship_left by 1
        stats.ships_left -= 1

        #empty aliens group and bullets group
        aliens.empty()
        bullets.empty()

        #create a new group of aliens, put the ship in the center bottom of the
        # screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #half
        sleep(0.5)
    else:
        stats.game_active = False

def check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''check if any aliens in the bottom of the screen'''
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            #deal like ship hit event
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''check if any alien at the edge of screen and update all aliens'
    position'''
    check_fleet_edges(ai_settings, aliens)
    #check any alien on the bottom of screen
    check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    aliens.update()

    #check collision between alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
