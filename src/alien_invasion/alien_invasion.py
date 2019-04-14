import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    play_button = Button(ai_settings,screen,"Play")
    
    ship = Ship(ai_settings,screen)                       
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        gf.check_events(ai_settings,stats,screen,play_button, ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens, bullets)
            gf.update_aliens(ai_settings,stats,screen,ship, aliens,bullets)
        gf.update_screen(ai_settings,stats,screen,ship,aliens,bullets,play_button)
        

run_game()

