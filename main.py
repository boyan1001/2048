import pygame, sys
from pygame.locals import *
import tools.UI as UI
import random
import json

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
MEDUIMSTATEBLUE = UI.hexToRgb('#9D53FF') # 中等藍色
TROPICALVIOLET = UI.hexToRgb('#D882F7') # 熱帶紫羅蘭
LAVENDER = UI.hexToRgb('#E0B0FF') # 薰衣草色
CHAMPAGNEPINK = UI.hexToRgb('#F7D9E1') # 香檳粉
SANDYBROWN = UI.hexToRgb('#FFB57D') # 沙褐色
SANDYBROWN2 = UI.hexToRgb('#FB9649') # 沙褐色2
BURNTSIENNA = UI.hexToRgb('#E76F51') # 焦土黃
ENGINEERINGORANGE = UI.hexToRgb('#D00000') # 工程橙
ROSEWOOD = UI.hexToRgb('#650000') # 紅木色
RICHBLACK = UI.hexToRgb('#03071E') # 濃黑色
GRAY3 = UI.hexToRgb('#918085') # 香檳粉
GRAY4 = UI.hexToRgb('#438572') # 灰色4


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

def gameBlockSetting():
    # block_set
    blocks_set = []
    # game page
    blocks = []
    blocks.append(UI.Block(pygame.Rect(0.73 * screen_width, 0.05 * screen_height, 0.23 * screen_width, 0.09 * screen_height), WHITE, '', SKYBLUE, title_font_link, 35, 0.05))
    blocks.append(UI.Block(pygame.Rect(0.47 * screen_width, 0.05 * screen_height, 0.23 * screen_width, 0.09 * screen_height), WHITE, '', SKYBLUE, title_font_link, 35, 0.05))
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
    return blocks_set

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
    records = []
    with open('./docs/record/records.json', 'r') as f:
        records = json.load(f)

    # read saves
    save = []
    now = []
    with open('./docs/save/save01.json', 'r') as f:
        save = json.load(f)

    # random generate a new block
    if save['initialized'] == False:
        save['initialized'] = True
        save['board'] = [[0 for i in range(4)] for j in range(4)]
        t = 0
    
        while t < 2:
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            if(save['board'][i][j] == 0):
                save['board'][i][j] = 2
                t += 1
        
        with open('./docs/save/save01.json', 'w') as f:
            json.dump(save, f)
    now = save['board']

    # pts counters setting
    hpts = records['player']['highest_pts']
    pts = save['pts']
    blocks_set = gameBlockSetting()
    hpts_title = UI.Text(title_font_link, 20, 'Best', TIFFANYBLUE, 0.845 * screen_width, 0.07 * screen_height)
    pts_title = UI.Text(title_font_link, 20, 'Points', TIFFANYBLUE, 0.585 * screen_width, 0.07 * screen_height)
    hpts_text = UI.Text(title_font_link, ptsCounterTextResize(hpts), str(hpts), AERO, 0.845 * screen_width, 0.115 * screen_height)
    pts_text = UI.Text(title_font_link, ptsCounterTextResize(pts), str(pts), AERO, 0.585 * screen_width, 0.115 * screen_height)

    # game block setting
    # GRAY3 = UI.hexToRgb('#918085') # 灰色3
    # GRAY4 = UI.hexToRgb('#438572') # 灰色4
    # AQUAMARINE = UI.hexToRgb('#80FFDB') # 水藍色
    # TURQUOISE = UI.hexToRgb('#72EFDD') # 藍綠色
    # TIFFANYBLUE = UI.hexToRgb('#64DFDF') # 蒂芙尼藍
    # SKYBLUE = UI.hexToRgb('#56CFE1') # 天藍色
    # AERO = UI.hexToRgb('#48BFE3') # 青色
    # PICTONBLUE = UI.hexToRgb('#4EA8DE') # 藍色
    # UNITEDNATIONSBLUE = UI.hexToRgb('#5390D9') # 聯合國藍
    # SLATEBLUE = UI.hexToRgb('#5E60CE') # 石板藍
    # GRAPE = UI.hexToRgb('#6930C3') # 葡萄色
    # FRENCHVOILET = UI.hexToRgb('#7400B8') # 紫羅蘭色
    # MEDUIMSTATEBLUE = UI.hexToRgb('#9D53FF') # 中等藍色
    # TROPICALVIOLET = UI.hexToRgb('#D882F7') # 熱帶紫羅蘭
    # LAVENDER = UI.hexToRgb('#E0B0FF') # 薰衣草色
    # CHAMPAGNEPINK = UI.hexToRgb('#F7D9E1') # 香檳粉
    # SANDYBROWN = UI.hexToRgb('#FFB57D') # 沙褐色
    # SANDYBROWN2 = UI.hexToRgb('#FB9649') # 沙褐色2
    # BURNTSIENNA = UI.hexToRgb('#E76F51') # 焦土黃
    # ENGINEERINGORANGE = UI.hexToRgb('#D00000') # 工程橙
    # ROSEWOOD = UI.hexToRgb('#650000') # 紅木色
    # RICHBLACK = UI.hexToRgb('#03071E') # 濃黑色
    dic = {
        -1: [GRAY3, WHITE],
        2: [AQUAMARINE, GRAY4],
        4: [TURQUOISE, GRAY4],
        8: [TIFFANYBLUE, WHITE],
        16: [SKYBLUE, WHITE],
        32: [AERO, WHITE],
        64: [PICTONBLUE, WHITE],
        128: [UNITEDNATIONSBLUE, WHITE],
        256: [SLATEBLUE, WHITE],
        512: [GRAPE, WHITE],
        1024: [FRENCHVOILET, WHITE],
        2048: [MEDUIMSTATEBLUE, WHITE],
        4096: [TROPICALVIOLET, WHITE],
        8192: [LAVENDER, WHITE],
        16384: [CHAMPAGNEPINK, GRAY3],
        32768: [SANDYBROWN, WHITE],
        65536: [SANDYBROWN2, WHITE],
        131072: [BURNTSIENNA, WHITE],
        262144: [ENGINEERINGORANGE, WHITE],
        524288: [ROSEWOOD, WHITE],
        1048576: [RICHBLACK, WHITE],
    }
    gameBlocks = []
    for i in range(4):
        for j in range(4):
            value = now[i][j]
            if value == 0:continue
            gap_w = 0.028
            gap_h = 0.018
            block_w = (0.92 - 5 * gap_w) / 4
            block_h = (0.6 - 5 * gap_h) / 4
            if(value not in dic):
                gameBlocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), dic[-1][0], 'error', dic[-1][1], title_font_link, 30, 0.05))
            elif(value > 1048576):
                gameBlocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), dic[1048576][0], str(1048576), dic[1048576][1], title_font_link, gameBlockTextResize(1048576), 0.05))
            else:
                gameBlocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), dic[value][0], str(value), dic[value][1], title_font_link, gameBlockTextResize(value), 0.05))

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
    hpts_text.drawText(screen)
    pts_text.drawText(screen)
    hpts_title.drawText(screen)
    pts_title.drawText(screen)
    # Draw the game board
    for block in blocks_set[1]:
        block.draw(screen)
    # Draw the game blocks
    for block in gameBlocks:
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
