'''
pygame day 1
using pygame.display
crate the main windows
'''
import time
import pygame

#init the pygame package
pygame.init()

# display.set_mode(resolution=(0,0), flag=0, depth=0)
# create the windows width:480, height:700
screan = pygame.display.set_mode((480, 700))

while True:
    time.sleep(5)

# quit the pygame
pygame.quit()
