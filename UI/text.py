import pygame, sys
from pygame.locals import *

class Text:
    def __init__(self, font_link, size, text, color, x, y):
        self.font_link = font_link
        self.size = size
        self.text = text
        self.color = color
        self.x = x
        self.y = y

    def drawText(self, surface):
        font_obj = pygame.font.Font(self.font_link, self.size) #創字體的物件
        text_surface = font_obj.render(self.text, True, self.color) #創文字Surface
        text_rect = text_surface.get_rect() #文字方塊
        text_rect.center = (self.x, self.y)
        
        surface.blit(text_surface, text_rect)

    def drawTextWithShadow(self, surface, shadow_color, shadow_offset):
        font_obj = pygame.font.Font(self.font_link, self.size) #創字體的物件
        text_surface = font_obj.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)

        text_shadow_surface = font_obj.render(self.text, True, shadow_color)
        text_shadow_rect = text_shadow_surface.get_rect()
        text_shadow_rect.center = (self.x + shadow_offset, self.y + shadow_offset)

        surface.blit(text_shadow_surface, text_shadow_rect)
        surface.blit(text_surface, text_rect)