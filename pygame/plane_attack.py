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


    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __update_sprites(self):
        '''使用sprite模块,更新角色位置和信息'''
        self.bg_sprites_group.draw(self.screen)
        self.bg_sprites_group.update()

        pass

    def __check_collision(self):
        '''检查飞机碰撞'''

    @staticmethod
    def __game_over():
        print("Game Over!")
        pygame.quit()
        exit()

if __name__ == '__main__':
    plane_game = PlaneGame()
    plane_game.game_start()

