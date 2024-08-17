import pygame, sys
from pygame.locals import *

def hexToRgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

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

# button
class Button(Text):
    def __init__(self, rect, color, text, text_color, font_link, font_size, key):
        self.rect = rect
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font_link = font_link
        self.font_size = font_size
        self.choose = False
        self.key = key

    def clickJudge(self, x, y):
        if self.rect.collidepoint(x, y):
            self.choose = True
        else:
            self.choose = False

    def draw(self, surface):
        if(self.choose):
            self.color, self.text_color = self.text_color, self.color
        
        x, y, w, h = self.rect
        radius = 0.2 * h
        pygame.draw.rect(surface, self.color, (x + radius, y, w - 2 * radius, h))  # 中心矩形
        pygame.draw.rect(surface, self.color, (x, y + radius, w, h - 2 * radius))  # 中心矩形
        pygame.draw.circle(surface, self.color, (x + radius, y + radius), radius)  # 左上角圓
        pygame.draw.circle(surface, self.color, (x + w - radius, y + radius), radius)  # 右上角圓
        pygame.draw.circle(surface, self.color, (x + radius, y + h - radius), radius)  # 左下角圓
        pygame.draw.circle(surface, self.color, (x + w - radius, y + h - radius), radius)  # 右下角圓
        txt = Text(self.font_link, self.font_size, self.text, self.text_color, x + 0.5 * w, y + 0.5 * h)
        txt.drawText(surface)
        if(self.choose):
            self.color, self.text_color = self.text_color, self.color

    def drawWithShadow(self, surface, shadow_color, offset):
        x, y, w, h = self.rect
        x += offset
        y += offset
        radius = 0.2 * h
        pygame.draw.rect(surface, shadow_color, (x + radius, y, w - 2 * radius, h))  # 中心矩形
        pygame.draw.rect(surface, shadow_color, (x, y + radius, w, h - 2 * radius))  # 中心矩形
        pygame.draw.circle(surface, shadow_color, (x + radius, y + radius), radius)  # 左上角圓
        pygame.draw.circle(surface, shadow_color, (x + w - radius, y + radius), radius)  # 右上角圓
        pygame.draw.circle(surface, shadow_color, (x + radius, y + h - radius), radius)  # 左下角圓
        pygame.draw.circle(surface, shadow_color, (x + w - radius, y + h - radius), radius)  # 右下角圓
        self.draw(surface)