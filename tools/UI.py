import pygame, sys
from pygame.locals import *

# Colors
def hexToRgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

WHITE = hexToRgb('#FFFFFF')
BLACK = hexToRgb('#000000')
GRAY = hexToRgb('#F2F2F2')
GRAY2 = hexToRgb('#E3E3E3')
BLUE1 = hexToRgb('#73C6D9')
BLUE2 = hexToRgb('#5EA3A3')
BLUE3 = hexToRgb('#3A656A')
BLUE4 = hexToRgb('#2E4E50')
BLUE5 = hexToRgb('#AAEBFF')
BEIGE = hexToRgb('#F2EBDC') # 米黃色
AQUAMARINE = hexToRgb('#B2FFD0') # 水藍色
TURQUOISE = hexToRgb('#72EFDD') # 藍綠色
TIFFANYBLUE = hexToRgb('#64DFDF') # 蒂芙尼藍
SKYBLUE = hexToRgb('#56CFE1') # 天藍色
AERO = hexToRgb('#48BFE3') # 青色
PICTONBLUE = hexToRgb('#4EA8DE') # 藍色
UNITEDNATIONSBLUE = hexToRgb('#5390D9') # 聯合國藍
SLATEBLUE = hexToRgb('#5E60CE') # 石板藍
GRAPE = hexToRgb('#6930C3') # 葡萄色
FRENCHVOILET = hexToRgb('#7400B8') # 紫羅蘭色
MEDUIMSTATEBLUE = hexToRgb('#9D53FF') # 中等藍色
TROPICALVIOLET = hexToRgb('#D882F7') # 熱帶紫羅蘭
LAVENDER = hexToRgb('#E0B0FF') # 薰衣草色
CHAMPAGNEPINK = hexToRgb('#F7D9E1') # 香檳粉
SANDYBROWN = hexToRgb('#FFB57D') # 沙褐色
SANDYBROWN2 = hexToRgb('#FB9649') # 沙褐色2
BURNTSIENNA = hexToRgb('#E76F51') # 焦土黃
ENGINEERINGORANGE = hexToRgb('#D00000') # 工程橙
ROSEWOOD = hexToRgb('#650000') # 紅木色
RICHBLACK = hexToRgb('#03071E') # 濃黑色
GRAY3 = hexToRgb('#918085') # 香檳粉
GRAY4 = hexToRgb('#438572') # 灰色4

# Text
def ptsCounterTextResize(pts):
    if pts < 10000:
        return 30
    elif pts < 100000:
        return 25
    elif pts < 1000000:
        return 20
    else:
        return 15

def gameBlockTextResize(value):
    if value < 100:
        return 45
    elif value < 1000:
        return 36
    elif value < 10000:
        return 28
    elif value < 100000:
        return 23
    elif value < 1000000:
        return 18
    else:
        return 15
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

# Block
class Block():
    def __init__(self, rect, color, text, text_color, font_link, font_size, radious_ratio):
        self.rect = rect
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font_link = font_link
        self.font_size = font_size
        self.radius_ratio = radious_ratio

    def draw(self, surface):
        x, y, w, h = self.rect
        radius = self.radius_ratio * h
        pygame.draw.rect(surface, self.color, (x + radius, y, w - 2 * radius, h))  # 中心矩形
        pygame.draw.rect(surface, self.color, (x, y + radius, w, h - 2 * radius))  # 中心矩形
        pygame.draw.circle(surface, self.color, (x + radius, y + radius), radius)  # 左上角圓
        pygame.draw.circle(surface, self.color, (x + w - radius, y + radius), radius)  # 右上角圓
        pygame.draw.circle(surface, self.color, (x + radius, y + h - radius), radius)  # 左下角圓
        pygame.draw.circle(surface, self.color, (x + w - radius, y + h - radius), radius)  # 右下角圓
        if(self.text != ''):
            txt = Text(self.font_link, self.font_size, self.text, self.text_color, x + 0.5 * w, y + 0.5 * h)
            txt.drawText(surface)

    def drawWithShadow(self, surface, shadow_color, offset):
        x, y, w, h = self.rect
        x += offset
        y += offset
        radius = self.radius_ratio * h
        pygame.draw.rect(surface, shadow_color, (x + radius, y, w - 2 * radius, h))  # 中心矩形
        pygame.draw.rect(surface, shadow_color, (x, y + radius, w, h - 2 * radius))  # 中心矩形
        pygame.draw.circle(surface, shadow_color, (x + radius, y + radius), radius)  # 左上角圓
        pygame.draw.circle(surface, shadow_color, (x + w - radius, y + radius), radius)  # 右上角圓
        pygame.draw.circle(surface, shadow_color, (x + radius, y + h - radius), radius)  # 左下角圓
        pygame.draw.circle(surface, shadow_color, (x + w - radius, y + h - radius), radius)  # 右下角圓
        self.draw(surface)

# Button
class Button():
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
        block = Block(self.rect, self.color, self.text, self.text_color, self.font_link, self.font_size, 0.2)
        block.draw(surface)
        if(self.choose):
            self.color, self.text_color = self.text_color, self.color

    def drawWithShadow(self, surface, shadow_color, offset):
        x, y, w, h = self.rect
        block = Block(self.rect, self.color, self.text, self.text_color, self.font_link, self.font_size, 0.2)
        block.drawWithShadow(surface, shadow_color, offset)
        self.draw(surface)