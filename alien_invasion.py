import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    # 1.初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    # 创建ship stat 的实例
    stats=GameStats(ai_settings)


    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 3.设置游戏标题
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship=Ship(ai_settings,screen)
    # 实例外星人
    alien=Alien(ai_settings,screen)
    # 创建一个编组存储子弹
    bullets=Group()
    # 创建一个编组存储外星人
    aliens=Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)
    # 创建一个button
    play_button=Button(ai_settings,screen,'Play')
    # 创建一个计分板实例
    scoreboard=Scoreboard(ai_settings,screen,stats)
    # 4.开始游戏的主循环
    while True:
        # 鼠标事件
        gf.check_event(ai_settings,screen,ship,aliens,bullets,stats,play_button,scoreboard)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,scoreboard)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings,screen,bullets,aliens,ship,scoreboard
            ,stats)
            gf.update_aliens(ai_settings,screen,ship,stats,aliens,bullets,scoreboard)
        else:
            pygame.mouse.set_visible(True)
run_game()
