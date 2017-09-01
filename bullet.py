import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen=screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        # 储存用小数表示的子弹位置
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
    def update(self):
        """子弹向上"""
        # y轴减去速度
        self.y-=self.speed_factor
        # 实际影响
        self.rect.y=self.y
    
