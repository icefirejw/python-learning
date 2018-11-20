'''
飞机大战的精灵模块，主要创建飞机经理类，用于图像管理
属性：image，rect， speed
方法：
 __init__(self, image_name, speed)
 update(self)
'''
import pygame

# define the screen size
SCREEN_REC = pygame.rect.Rect(0,0,480,700)
FRAME_PER_SEC = 60

class PlaneSprites(pygame.sprite.Sprite):
    def __init__(self, image_name, speed = 1):

        # 一定要先通过父类的初始化函数来继承
        super().__init__()
        '''
        初始化三个属性：
            image
            rect
            speed
        '''
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''
        必须重写update方法，用于精灵组调用
        更新图像位置
        '''
        self.rect.y += self.speed

class Background(PlaneSprites):
    '''背景图像的精灵类'''

    def update(self):
        # 1. 调用父类的update函数，已实现y移动方法
        super().update()

        # 2. 判断图像是否移除了屏幕，如果移出了屏幕，则到屏幕的最上方
        if self.rect.y >= SCREEN_REC.height:
            self.rect.y = -self.rect.height
