import pygame, sys
from pygame.locals import *

# color
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

# screen setting
screen_width = 800
screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('2048')

fontObj = pygame.font.Font('./Assets/font/Cubic_11_1.100_R.ttf', 60) #創字體的物件
textSurfaceObj = fontObj.render('2048 GAME', True, BLACK) #創文字Surface
textRectObj = textSurfaceObj.get_rect() #文字方塊
textRectObj.center = (0.5 * screen_width, 0.2 * screen_height)