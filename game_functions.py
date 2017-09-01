import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
def check_event(ai_settings,screen,ship,aliens,bullets,stats,play_button,scoreboard):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_event(ai_settings,screen,stats,aliens,event,ship,bullets,scoreboard)
        elif event.type==pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,ship,aliens,bullets,play_button,mouse_x,mouse_y,scoreboard)
def check_play_button(ai_settings,screen,stats,ship,aliens,bullets,play_button,mouse_x,mouse_y,scoreboard):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        start_game(ai_settings,screen,stats,aliens,bullets,ship,scoreboard)
def check_keydown_event(ai_settings,screen,stats,aliens,event,ship,bullets,scoreboard):
            if event.key==pygame.K_RIGHT:
                # 飞船向右移动
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                # 飞船向左移动
                ship.moving_left=True
            elif event.key==pygame.K_SPACE:
                # 开火
                fire_bullet(ai_settings,screen,ship,bullets)
            elif event.key==pygame.K_q:
                # 按键q退出游戏
                sys.exit()
            elif event.key==pygame.K_p:
                start_game(ai_settings,screen,stats,aliens,bullets,ship,scoreboard)
def start_game(ai_settings,screen,stats,aliens,bullets,ship,scoreboard):
    pygame.mouse.set_visible(False)
    # 初始化游戏设置
    ai_settings.initialize_dynamic_settings()
    # 重置游戏统计信息
    stats.reset_stats()
    scoreboard.prep_score()
    scoreboard.prep_level()
    stats.game_active=True

    # 清空外星人和子弹
    aliens.empty()
    bullets.empty()

    # 重新绘制屏幕
    create_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
def check_keyup_event(event,ship):
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left=False

def update_bullets(ai_settings,screen,bullets,aliens,ship,scoreboard
,stats):
    for bullet in bullets.copy():
        if bullet.rect.top<=0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(ai_settings,screen,bullets,aliens,ship,scoreboard,stats)

def check_bullets_aliens_collisions(ai_settings,screen,bullets,aliens,ship,scoreboard,stats):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increas_speed()
        stats.level+=1
        scoreboard.prep_level()
        create_fleet(ai_settings,screen,aliens,ship)
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            scoreboard.prep_score()
            scoreboard.prep_ships()
        check_high_score(stats,scoreboard)

def update_aliens(ai_settings,screen,ship,stats,aliens,bullets,scoreboard):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,ship,stats,aliens,bullets,scoreboard)
    check_aliens_bottom(ai_settings,screen,ship,stats,aliens,bullets,scoreboard)
def check_aliens_bottom(ai_settings,screen,ship,stats,aliens,bullets,scoreboard):
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen.get_rect().bottom:
            ship_hit(ai_settings,screen,ship,stats,aliens,bullets,scoreboard)
            break
def check_high_score(stats,scoreboard):
    if stats.high_score<=stats.score:
        stats.high_score=stats.score
        scoreboard.prep_high_score()
def ship_hit(ai_settings,screen,ship,stats,aliens,bullets,scoreboard):
    # 生命减1

    if stats.ship_left>0:
        stats.ship_left-=1
        scoreboard.prep_ships()
    else:
        stats.game_active=False

    # 清空屏幕
    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings,screen,aliens,ship)
    # 创建新的外星人和飞船顺序错了
    #create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()
    # 暂停0.5
    sleep(0.5)
def check_fleet_edges(ai_settings,aliens):
    """移动外星人群"""
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direction(ai_settings,aliens)
            break;
def check_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullet_allowed:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings,screen,aliens,ship):
    """绘制需要的外星人"""
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    number_alien_x=get_number_aliens_x(ai_settings,alien_width)
    number_rows=get_number_aliens_y(ai_settings,alien_height,ship)
    for number_row in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,number_row,alien_height,alien_width)
def get_number_aliens_x(ai_settings,alien_width):
    available_space=ai_settings.screen_width-2*alien_width
    number_alien_x=int(available_space / (2*alien_width))
    return number_alien_x
def get_number_aliens_y(ai_settings,alien_height,ship):
    available_space=ai_settings.screen_height-3*alien_height
    number_rows=int(available_space/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,number_rows,alien_height,alien_width):
    alien=Alien(ai_settings,screen)
    alien.rect.x=alien_width+2*alien_width*alien_number
    alien.rect.y=alien_height+alien_height*2*number_rows
    aliens.add(alien)
def update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,scoreboard):
    """更新屏幕上的图像，并切换新的屏幕"""

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    scoreboard.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
