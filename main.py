import pygame, sys
from UI import text, button, colors
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


# Screen setting
FPS = 60
screen_width = 400
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')
page_value = 0

# Font
title_font_link = './Assets/font/Roboto-Bold.ttf'

# draw text
title = text.Text(title_font_link, 100, '2048', WHITE, 0.5 * screen_width, 0.2 * screen_height)

# buttons_set
buttons_set = []
# home page
buttons = []
buttons.append(button.Button(pygame.Rect(0.2 * screen_width, 0.45 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UNITEDNATIONSBLUE, 'START', WHITE, title_font_link, 35, '0to1'))
buttons.append(button.Button(pygame.Rect(0.2 * screen_width, 0.575 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UNITEDNATIONSBLUE, 'SETTING', WHITE, title_font_link, 35, '0to2'))
buttons.append(button.Button(pygame.Rect(0.2 * screen_width, 0.7 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UNITEDNATIONSBLUE, 'ABOUTUS', WHITE, title_font_link, 35, '0to3'))
buttons_set.append(buttons)

# image
home_page_background = pygame.image.load('./Assets/image/home_page_background.png')
home_page_background = pygame.transform.scale(home_page_background, (screen_width, screen_height * 1.2))
home_page_background.convert()

def home_page():
    # Draw the screen
    screen.fill(TURQUOISE)
    screen.blit(home_page_background, (0, 0))
    # screen.blit(title_shadow_surface, title_shadow_rect)
    title.drawTextWithShadow(screen, AERO, 2)
    # Draw the button
    for button in buttons_set[0]:
        button.draw(screen)

while True:
    clock.tick(FPS)
    # Event handing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        x, y = pygame.mouse.get_pos()
        for button in buttons_set[page_value]:
            button.clickJudge(x, y)
        if event.type == MOUSEBUTTONDOWN:
            for button in buttons_set[page_value]:
                if button.choose:
                    print(button.key)
    
    if(page_value == 0):
        home_page()

    # Update the screen
    pygame.display.update()
