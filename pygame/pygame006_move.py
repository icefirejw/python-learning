'''
pygame learning: update
'''
import pygame

# import locals module for EVENT
from pygame.locals import*

# initialize the pygame module 
pygame.init()

#craate the main windows
screan = pygame.display.set_mode((480,700),0, 32)
pygame.display.set_caption('Plane Exercise!')

# draw backgroud
bg = pygame.image.load("./plane_images/background.png")
screan.blit(bg,(0,0))

# draw the hero plane
hero = pygame.image.load("./plane_images/me1.png")
screan.blit(hero,(150,500))

# update the screan
pygame.display.update()

# <1 设定hero plane的矩形，用于定义飞机位置
hero_rect = pygame.rect.Rect(150,500,102,126)

# 设定循环周期
clock = pygame.time.Clock()

# main game loop
while True:
    # 必须使用事件获取，如果只是使用pass或其他死循环，无法现实图片
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    # 设定循环频率
    clock.tick(60)

    # <2 移动飞机，设定飞机位置
    hero_rect.y -= 1
    screan.blit(bg, (0,0)) # 必须刷新背景，否则会留下飞机残影
    screan.blit(hero, hero_rect)

    # <3 刷新图像
    pygame.display.update()

