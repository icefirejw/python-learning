'''
pygame day 1
using pygame.display
crate the main windows
'''
import pygame

def draw_image(win, img, x=0, y=0):
    # draw the backgrand images
    # 1> load the image
    image = pygame.image.load(img)
    # 2> blit to draw the image
    #    blit(image, (x, y))
    win.blit(image, (x,y))
    # 3> update the screan
    pygame.display.update()
    return image
    
#init the pygame package
pygame.init()

# display.set_mode(resolution=(0,0), flag=0, depth=0)
# create the windows width:480, height:700
screan = pygame.display.set_mode((480, 700))

# draw the backgrand images
draw_image(win=screan, img="./plane_images/background.png")

# draw the hero plane
draw_image(win=screan, img="./plane_images/me1.png", x=150, y=500)

# quit the pygame
while True:
    act = input("the next action? 'q!' to quit: ")
    if act=='q!':
        pygame.quit()
        exit()
