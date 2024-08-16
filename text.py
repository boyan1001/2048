import pygame, sys
from pygame.locals import *

def drawText(font_link, size, text, color, x, y):
    font_obj = pygame.font.Font(font_link, size) #創字體的物件
    text_surface = font_obj.render(text, True, color) #創文字Surface
    text_rect = text_surface.get_rect() #文字方塊
    text_rect.center = (x, y)
    return text_surface, text_rect