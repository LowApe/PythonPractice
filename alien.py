import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()

        # 初始化外星人
        self.screen=screen
        self.ai_settings=ai_settings

        # 加载图片
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        # 定位
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        # 存储外星人的准确定位
        self.x=float(self.rect.x)

    def update(self):
        self.rect.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘,就返回True"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def blitme(self):
        self.screen.blit(self.image,self.rect)
