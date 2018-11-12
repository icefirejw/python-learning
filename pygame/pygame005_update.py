'''
pygame learning: update
'''
import pygame
import sys
# import locals module for EVENT
from pygame.locals import*

# initialize the pygame module 
pygame.init()

#craate the main windows
main_win = pygame.display.set_mode((480,700),0, 32)
pygame.display.set_caption('Plane Exercise!')

# draw backgroud
bg = pygame.image.load("./plane_images/background.png")
main_win.blit(bg,(0,0))

# draw the hero plane
hero = pygame.image.load("./plane_images/me1.png")
main_win.blit(hero,(150,500))

# update the screan
pygame.display.update()

# main game loop
while True:
    # 必须使用事件获取，如果只是使用pass或其他死循环，无法现实图片
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()