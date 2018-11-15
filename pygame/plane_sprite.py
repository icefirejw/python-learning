'''
飞机大战的精灵模块，主要创建飞机经理类，用于图像管理
属性：image，rect， speed
方法：
 __init__(self, image_name, speed)
 update(self)
'''
import pygame

WIN_WIDTH = 480
WIN_HEIGHT = 700
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