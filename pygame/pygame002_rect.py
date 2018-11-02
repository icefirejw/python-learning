'''
pygame day 1
using pygame.Rect
'''

import pygame

#Rect(x, y, width, height)
hero_rect = pygame.Rect(100, 200, 120, 250)

# print the rect's position
print("the rect's position is (%d, %d)" % (hero_rect.x, hero_rect.y))
# print the rect's size
print("the rect's size is (%d, %d)" % (hero_rect.width, hero_rect.height)) 
print("the rect's size is: %d %d" % hero_rect.size)
