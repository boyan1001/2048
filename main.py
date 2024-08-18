import pygame, sys
from pygame.locals import *
import tools.UI as UI

# Colors
WHITE = UI.hexToRgb('#FFFFFF')
BLACK = UI.hexToRgb('#000000')
GRAY = UI.hexToRgb('#F2F2F2')
GRAY2 = UI.hexToRgb('#E3E3E3')
BLUE1 = UI.hexToRgb('#73C6D9')
BLUE2 = UI.hexToRgb('#5EA3A3')
BLUE3 = UI.hexToRgb('#3A656A')
BLUE4 = UI.hexToRgb('#2E4E50')
BLUE5 = UI.hexToRgb('#AAEBFF')
BEIGE = UI.hexToRgb('#F2EBDC') # 米黃色
AQUAMARINE = UI.hexToRgb('#80FFDB') # 水藍色
TURQUOISE = UI.hexToRgb('#72EFDD') # 藍綠色
TIFFANYBLUE = UI.hexToRgb('#64DFDF') # 蒂芙尼藍
SKYBLUE = UI.hexToRgb('#56CFE1') # 天藍色
AERO = UI.hexToRgb('#48BFE3') # 青色
PICTONBLUE = UI.hexToRgb('#4EA8DE') # 藍色
UNITEDNATIONSBLUE = UI.hexToRgb('#5390D9') # 聯合國藍
SLATEBLUE = UI.hexToRgb('#5E60CE') # 石板藍
GRAPE = UI.hexToRgb('#6930C3') # 葡萄色
FRENCHVOILET = UI.hexToRgb('#7400B8') # 紫羅蘭色


# Screen setting
FPS = 60
screen_width = 400
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')
now_page_value = 0
prev_page_value = 0
# button_colddown_time = 0

# Font
title_font_link = './docs/asset/font/Roboto-Bold.ttf'

# draw text
# open title
open_title = UI.Text(title_font_link, 100, '2048', WHITE, 0.5 * screen_width, 0.2 * screen_height)
# game title
game_title = UI.Text(title_font_link, 70, '2048', WHITE, 0.24 * screen_width, 0.1 * screen_height)
quote_text = UI.Text(title_font_link, 14, 'Join the numbers and get to the 2048 tile!', WHITE, 0.378 * screen_width, 0.185 * screen_height)

# block_set
blocks_set = []
# game page
blocks = []
blocks.append(UI.Block(pygame.Rect(0.73 * screen_width, 0.05 * screen_height, 0.23 * screen_width, 0.09 * screen_height), WHITE, '', WHITE, title_font_link, 35, 0.05))
blocks.append(UI.Block(pygame.Rect(0.47 * screen_width, 0.05 * screen_height, 0.23 * screen_width, 0.09 * screen_height), WHITE, '', WHITE, title_font_link, 35, 0.05))
blocks.append(UI.Block(pygame.Rect(0.04 * screen_width, 0.3* screen_height, 0.92 * screen_width, 0.6 * screen_height), WHITE, '', WHITE, title_font_link, 35, 0.05))
blocks_set.append(blocks)
blocks = []
gap_w = 0.028
gap_h = 0.018
block_w = (0.92 - 5 * gap_w) / 4
# block_h = 0.1125
block_h = (0.6 - 5 * gap_h) / 4
for i in range(4):
    for j in range(4):
        blocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), GRAY2, '', WHITE, title_font_link, 35, 0.05))
blocks_set.append(blocks)

# buttons_set
buttons_set = []
# home page
buttons = []
buttons.append(UI.Button(pygame.Rect(0.2 * screen_width, 0.45 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UNITEDNATIONSBLUE, 'START', WHITE, title_font_link, 35, '0to1'))
buttons.append(UI.Button(pygame.Rect(0.2 * screen_width, 0.575 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UNITEDNATIONSBLUE, 'SETTING', WHITE, title_font_link, 35, '0to2'))
buttons.append(UI.Button(pygame.Rect(0.2 * screen_width, 0.7 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UNITEDNATIONSBLUE, 'ABOUTUS', WHITE, title_font_link, 35, '0to3'))
buttons_set.append(buttons)
# game page
buttons = []
buttons.append(UI.Button(pygame.Rect(0.73 * screen_width, 0.16 * screen_height, 0.23 * screen_width, 0.05 * screen_height), TIFFANYBLUE, 'MENU', WHITE, title_font_link, 20, '1to0'))
buttons_set.append(buttons)

# image
# home_page_backbround
home_page_background = pygame.image.load('./docs/asset/image/home_page_background.png')
home_page_background = pygame.transform.scale(home_page_background, (screen_width, screen_height * 1.2))
home_page_background.convert()
# game_page_background
game_page_background = pygame.image.load('./docs/asset/image/game_page_background.png')
game_page_background = pygame.transform.scale(game_page_background, (screen_width, screen_height * 1.2))
game_page_background.convert()


def homePage():
    # Draw the screen
    screen.fill(TURQUOISE)
    screen.blit(home_page_background, (0, 0))
    # screen.blit(title_shadow_surface, title_shadow_rect)
    open_title.drawTextWithShadow(screen, AERO, 2)
    # Draw the button
    for button in buttons_set[0]:
        button.drawWithShadow(screen, SLATEBLUE, 3)

def gamePage():
    # read records
    # Draw the screen
    screen.fill(PICTONBLUE)
    screen.blit(game_page_background, (0, 0))
    game_title.drawTextWithShadow(screen, AERO, 2)
    quote_text.drawText(screen)

    # Draw the button
    for button in buttons_set[1]:
        button.drawWithShadow(screen, UNITEDNATIONSBLUE, 3)
    # Draw the score counter block and the history highest score block
    for block in blocks_set[0]:
        block.drawWithShadow(screen, UNITEDNATIONSBLUE, 3)
    # Draw the game board
    for block in blocks_set[1]:
        block.draw(screen)

    # write records

while True:
    clock.tick(FPS)
    # Event handing
    # if(button_colddown_time > 0):
        # button_colddown_time -= 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        x, y = pygame.mouse.get_pos()
        # if button_colddown_time != 0:break
        for button in buttons_set[now_page_value]:
            button.clickJudge(x, y)
        if event.type == MOUSEBUTTONDOWN:
            for button in buttons_set[now_page_value]:
                if button.choose:
                    print(button.key)
                    keyline = button.key.split('to')
                    prev_page_value = int(keyline[0])
                    now_page_value = int(keyline[1])
                    print(prev_page_value, now_page_value)
                    button.choose = False
                    break
                    # button_colddown_time = 10
    
    if(now_page_value == 0):
        homePage()
    elif(now_page_value == 1):
        gamePage()

    # Update the screen
    pygame.display.update()
