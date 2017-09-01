class Settings():
    """储存游戏的所有设置的类"""
    def __init__(self):
        """初始化屏幕的设置"""
        # 屏幕的设置
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)
        # 飞船设置
        self.ship_speed_factor=3
        self.ship_limit=3
        #子弹设置
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullet_allowed=5

        # 外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        # 1 表示向右 -1 表示想做
        self.fleet_direction=1
        # 添加游戏节奏的比例
        self.speedup_scale=1.1
        #计分比例
        self.aliens_score=1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        # 初始化随游戏的变化而变化的设置
        self.ship_speed_factor=3
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1
        # 计分
        self.alien_points=50
    def increas_speed(self):
        """提高速度设置"""
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.aliens_score)
