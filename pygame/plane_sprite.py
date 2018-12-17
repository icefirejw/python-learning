'''
飞机大战的精灵模块，主要创建飞机经理类，用于图像管理
属性：image，rect， speed
方法：
 __init__(self, image_name, speed)
 update(self)
'''
import random
import pygame

# define the screen size
SCREEN_REC = pygame.rect.Rect(0,0,480,700)
FRAME_PER_SEC = 60
CREATE_ENEMY_PLANE = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
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

class Background(GameSprite):
    '''背景图像的精灵类'''
    def __init__(self, is_alt=False):
        super().__init__("./plane_images/background.png")
        if is_alt:
            #如果是填充的图片，则需要将图片上移到原来图片的正上方进行拼接
            self.rect.bottom = 0

    def update(self):
        # 1. 调用父类的update函数，已实现y移动方法
        super().update()

        # 2. 判断图像是否移出了屏幕，如果移出了屏幕，则返回到屏幕的最上方
        if self.rect.y >= SCREEN_REC.height:
            self.rect.y = -self.rect.height

class EnemySprite(GameSprite):
    def __init__(self):
        #调用父类init函数，加载enemy plane 图片
        super().__init__('./plane_images/enemy1.png')
        # define the enemy plane's speed
        self.speed = random.randint(1,3)

        # define the enemy plane's position
        # the enemy's x is a random in the screen
        self.rect.x = random.randint(0, SCREEN_REC.width-self.rect.width)

    def update(self):
        super().update()

        # if the eneny is out of the screen, then kill itself.
        if (self.rect.y > SCREEN_REC.bottom):
            self.kill()

    #def __del__(self):
    #    print("deleting my self...")

class HeroPlaneSprite(GameSprite):
    '''define the hero plane'''
    def __init__(self):
        super().__init__("./plane_images/me1.png")

        #define the hero's position 
        self.rect.bottom = SCREEN_REC.bottom - 120
        self.rect.centerx = SCREEN_REC.centerx

        # define the bullet sprite group
        self.bullets = pygame.sprite.Group()
    
    def update(self):
        self.rect.x += self.speed

        if (self.rect.left <= SCREEN_REC.left):
            self.rect.left = SCREEN_REC.left
        
        if (self.rect.right >= SCREEN_REC.right):
            self.rect.right = SCREEN_REC.right
    
    def fire(self):
       
        # fire 3 bullets for one time
        for i in range(3):
            # init the buttle sprint
            buttle = BulletSprite()
   
            # init the buttle's position
            buttle.rect.bottom = self.rect. y - 20*i
            buttle.rect.centerx = self.rect.centerx
            # add the buttle to sprite group 
            self.bullets.add(buttle)

class BulletSprite(GameSprite):
    '''defined the bullet sprint '''
    def __init__(self):
        super().__init__('./plane_images/bullet1.png')
        self.speed = -2
    
    def update(self):
        super().update()
        if self.rect.y < SCREEN_REC.top:
            self.kill()
