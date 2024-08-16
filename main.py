import pygame, sys
from UI import colors
from UI import text
from UI import button
from pygame.locals import *

# Colors
WHITE = colors.hexToRgb('#FFFFFF')
BLACK = colors.hexToRgb('#000000')
GRAY = colors.hexToRgb('#574D4D')
GRAY2 = colors.hexToRgb('#B39E9E')
BLUE1 = colors.hexToRgb('#73C6D9')
BLUE2 = colors.hexToRgb('#5EA3A3')
BLUE3 = colors.hexToRgb('#3A656A')
BLUE4 = colors.hexToRgb('#2E4E50')
BLUE5 = colors.hexToRgb('#AAEBFF')
BEIGE = colors.hexToRgb('#F2EBDC') # 米黃色

AQUAMARINE = colors.hexToRgb('#80FFDB') # 水藍色
TURQUOISE = colors.hexToRgb('#72EFDD') # 藍綠色
TIFFANYBLUE = colors.hexToRgb('#64DFDF') # 蒂芙尼藍
SKYBLUE = colors.hexToRgb('#56CFE1') # 天藍色
AERO = colors.hexToRgb('#48BFE3') # 青色
PICTONBLUE = colors.hexToRgb('#4EA8DE') # 藍色
UNITEDNATIONSBLUE = colors.hexToRgb('#5390D9') # 聯合國藍
SLATEBLUE = colors.hexToRgb('#5E60CE') # 石板藍
GRAPE = colors.hexToRgb('#6930C3') # 葡萄色
FRENCHVOILET = colors.hexToRgb('#7400B8') # 紫羅蘭色


# Screen
FPS = 60
screen_width = 400
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')

# Font
title_font_link = './Assets/font/Roboto-Bold.ttf'

# draw text
title = text.Text(title_font_link, 100, '2048', WHITE, 0.5 * screen_width, 0.2 * screen_height)
# title_shadow_surface , title_shadow_rect = text.drawText(title_font_link, 80, '2048', GRAY, 0.5 * screen_width + 2, 0.2 * screen_height + 2)

buttons =[]
buttons.append(button.Button(pygame.Rect(0.2 * screen_width, 0.45 * screen_height, 0.6 * screen_width, 0.1 * screen_height), AERO, 'START', WHITE, title_font_link, 35))
buttons.append(button.Button(pygame.Rect(0.2 * screen_width, 0.575 * screen_height, 0.6 * screen_width, 0.1 * screen_height), AERO, 'SETTING', WHITE, title_font_link, 35))
buttons.append(button.Button(pygame.Rect(0.2 * screen_width, 0.7 * screen_height, 0.6 * screen_width, 0.1 * screen_height), AERO, 'ABOUTUS', WHITE, title_font_link, 35))
while True:
    clock.tick(FPS)
    # Event handing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        x, y = pygame.mouse.get_pos()
        for button in buttons:
            button.clickJudge(x, y)
        if event.type == MOUSEBUTTONDOWN:
            for button in buttons:
                if button.choose:
                    print(button.text)

    # Draw the screen
    screen.fill(TURQUOISE)
    # screen.blit(title_shadow_surface, title_shadow_rect)
    title.drawTextWithShadow(screen, AERO, 2)
    # Draw the button
    for button in buttons:
        button.draw(screen)

    # Update the screen
    pygame.display.update()
