import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        """初始化飞船，并初始化位置"""
        self.screen=screen
        self.ai_settings=ai_settings


        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        # 获取飞船的外部的矩形
        self.rect = self.image.get_rect()
        # 获取屏幕的矩形
        self.screen_rect=self.screen.get_rect()


        # 将每艘飞船放入到屏幕的中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom


        # 给飞船的属性centerx中存储小数值
        self.center=float(self.rect.centerx)



        # 左右移动的标志
        self.moving_right=False
        self.moving_left=False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor
        # 根据self.center 更新rect对象
        self.rect.centerx=self.center
    def center_ship(self):
        self.center=self.screen_rect.centerx
