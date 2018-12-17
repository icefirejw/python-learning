'''
plane attack main program
'''
import pygame
from plane_sprite import *

class PlaneGame(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 定义窗口
        self.screen = pygame.display.set_mode(SCREEN_REC.size)
        # 定义循环时钟
        self.clock = pygame.time.Clock()
        # 定义图像精灵和精灵组
        self.__create_sprites()
        # define the timer for enemy plane presenting
        # present, each 1 secend
        pygame.time.set_timer(CREATE_ENEMY_PLANE, 1000) 
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def game_start(self):
        print("start game ...")
        while True:
            # 设置循环频率
            self.clock.tick(FRAME_PER_SEC)
            # 处理游戏事件
            self.__event_handler()
            # 检查飞机碰撞
            self.__check_collision()
            # 更新游戏图像
            self.__update_sprites()
            # 刷新游戏图像
            pygame.display.update()

    def __create_sprites(self):
        '''创建游戏角色图像精灵和精灵组'''
        print("create sprints...")
        bg1 = Background()
        bg2 = Background(True)
        self.bg_sprites_group = pygame.sprite.Group(bg1,bg2)

        # create the enemy sprites group 
        self.enemy_group = pygame.sprite.Group()

        # create the hero plane sprite and group
        self.hero_plane = HeroPlaneSprite()
        self.hero_plane_group = pygame.sprite.Group(self.hero_plane)


    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_PLANE:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero_plane.fire()
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("to right")
        
        # get which key pressed by keyboard method 
        key_pressed = pygame.key.get_pressed()
        if (key_pressed[pygame.K_RIGHT]):
            self.hero_plane.speed = 2
        elif (key_pressed[pygame.K_LEFT]):
            self.hero_plane.speed = -2
        else:
            self.hero_plane.speed = 0


    def __update_sprites(self):
        '''使用sprite模块,更新角色位置和信息'''
        self.bg_sprites_group.draw(self.screen)
        self.bg_sprites_group.update()

        # update & draw the enemy plane 
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        
        # update & draw the hero plane
        self.hero_plane_group.update()
        self.hero_plane_group.draw(self.screen)

        # update & draw the bullet
        self.hero_plane.bullets.update()
        self.hero_plane.bullets.draw(self.screen)

    def __check_collision(self):
        '''检查飞机碰撞'''
        # 子弹打中了敌机 
        pygame.sprite.groupcollide(self.hero_plane.bullets, self.enemy_group,True, True)

        # 飞机碰到敌机 
        col_list = pygame.sprite.spritecollide(self.hero_plane, self.enemy_group, True)

        # 判断敌机是否碰到了飞机
        if len(col_list) > 0:
            self.hero_plane.kill()
            PlaneGame.__game_over()


    @staticmethod
    def __game_over():
        print("Game Over!")
        pygame.quit()
        exit()

if __name__ == '__main__':
    plane_game = PlaneGame()
    plane_game.game_start()

