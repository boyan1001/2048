import pygame, sys
from pygame.locals import *
import tools.UI as UI
import random
import json

# UI.WHITE = hexToRgb('#FFFFFF')
# UI.BLACK = hexToRgb('#000000')
# UI.GRAY = hexToRgb('#F2F2F2')
# UI.GRAY2 = hexToRgb('#E3E3E3')
# BLUE1 = hexToRgb('#73C6D9')
# BLUE2 = hexToRgb('#5EA3A3')
# BLUE3 = hexToRgb('#3A656A')
# BLUE4 = hexToRgb('#2E4E50')
# BLUE5 = hexToRgb('#AAEBFF')
# BEIGE = hexToRgb('#F2EBDC') # 米黃色
# UI.GRAY3 = UI.hexToRgb('#918085') # 灰色3
# UI.GRAY4 = UI.hexToRgb('#438572') # 灰色4
# UI.AQUAMARINE = UI.hexToRgb('#80FFDB') # 水藍色
# UI.TURQUOISE = UI.hexToRgb('#72EFDD') # 藍綠色
# UI.TIFFANYBLUE = UI.hexToRgb('#64DFDF') # 蒂芙尼藍
# UI.SKYBLUE = UI.hexToRgb('#56CFE1') # 天藍色
# UI.AERO = UI.hexToRgb('#48BFE3') # 青色
# UI.PICTONBLUE = UI.hexToRgb('#4EA8DE') # 藍色
# UI.UNITEDNATIONSBLUE = UI.hexToRgb('#5390D9') # 聯合國藍
# UI.SLATEBLUE = UI.hexToRgb('#5E60CE') # 石板藍
# UI.GRAPE = UI.hexToRgb('#6930C3') # 葡萄色
# UI.FRENCHVOILET = UI.hexToRgb('#7400B8') # 紫羅蘭色
# UI.MEDUIMSTATEBLUE = UI.hexToRgb('#9D53FF') # 中等藍色
# UI.TROPICALVIOLET = UI.hexToRgb('#D882F7') # 熱帶紫羅蘭
# UI.LAVENDER = UI.hexToRgb('#E0B0FF') # 薰衣草色
# UI.CHAMPAGNEPINK = UI.hexToRgb('#F7D9E1') # 香檳粉
# UI.SANDYBROWN = UI.hexToRgb('#FFB57D') # 沙褐色
# UI.SANDYBROWN2 = UI.hexToRgb('#FB9649') # 沙褐色2
# UI.BURNTSIENNA = UI.hexToRgb('#E76F51') # 焦土黃
# UI.ENGINEERINGORANGE = UI.hexToRgb('#D00000') # 工程橙
# UI.ROSEWOOD = UI.hexToRgb('#650000') # 紅木色
# UI.RICHBLACK = UI.hexToRgb('#03071E') # 濃黑色

# game title
title_font_link = './docs/asset/font/Roboto-Bold.ttf'
screen_width = 400
screen_height = 600
game_title = UI.Text(title_font_link, 70, '2048', UI.WHITE, 0.24 * screen_width, 0.1 * screen_height)
quote_text = UI.Text(title_font_link, 14, 'Join the numbers and get to the 2048 tile!', UI.WHITE, 0.378 * screen_width, 0.185 * screen_height)

def gameButtonSetting():
    buttons = []
    buttons.append(UI.Button(pygame.Rect(0.73 * screen_width, 0.16 * screen_height, 0.23 * screen_width, 0.05 * screen_height), UI.TIFFANYBLUE, 'MENU', UI.WHITE, title_font_link, 20, '1to0'))
    return buttons

def gameBlockSetting():
    # block_set
    blocks_set = []
    # game page
    blocks = []
    blocks.append(UI.Block(pygame.Rect(0.73 * screen_width, 0.05 * screen_height, 0.23 * screen_width, 0.09 * screen_height), UI.WHITE, '', UI.SKYBLUE, title_font_link, 35, 0.05))
    blocks.append(UI.Block(pygame.Rect(0.47 * screen_width, 0.05 * screen_height, 0.23 * screen_width, 0.09 * screen_height), UI.WHITE, '', UI.SKYBLUE, title_font_link, 35, 0.05))
    blocks.append(UI.Block(pygame.Rect(0.04 * screen_width, 0.3* screen_height, 0.92 * screen_width, 0.6 * screen_height), UI.WHITE, '', UI.WHITE, title_font_link, 35, 0.05))
    blocks_set.append(blocks)
    blocks = []
    gap_w = 0.028
    gap_h = 0.018
    block_w = (0.92 - 5 * gap_w) / 4
    # block_h = 0.1125
    block_h = (0.6 - 5 * gap_h) / 4
    for i in range(4):
        for j in range(4):
            blocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), UI.GRAY2, '', UI.WHITE, title_font_link, 35, 0.05))
    blocks_set.append(blocks)
    return blocks_set

def gamePage(records, save, screen, game_page_background, buttons, now):
    # pts counters setting
    hpts = records['player']['highest_pts']
    pts = save['pts']
    blocks_set = gameBlockSetting()
    hpts_title = UI.Text(title_font_link, 20, 'Best', UI.TIFFANYBLUE, 0.845 * screen_width, 0.07 * screen_height)
    pts_title = UI.Text(title_font_link, 20, 'Points', UI.TIFFANYBLUE, 0.585 * screen_width, 0.07 * screen_height)
    hpts_text = UI.Text(title_font_link, UI.ptsCounterTextResize(hpts), str(hpts), UI.AERO, 0.845 * screen_width, 0.115 * screen_height)
    pts_text = UI.Text(title_font_link, UI.ptsCounterTextResize(pts), str(pts), UI.AERO, 0.585 * screen_width, 0.115 * screen_height)

    # game block setting
    dic = {
        -1: [UI.GRAY3, UI.WHITE],
        2: [UI.AQUAMARINE, UI.GRAY4],
        4: [UI.TURQUOISE, UI.GRAY4],
        8: [UI.TIFFANYBLUE, UI.WHITE],
        16: [UI.SKYBLUE, UI.WHITE],
        32: [UI.AERO, UI.WHITE],
        64: [UI.PICTONBLUE, UI.WHITE],
        128: [UI.UNITEDNATIONSBLUE, UI.WHITE],
        256: [UI.SLATEBLUE, UI.WHITE],
        512: [UI.GRAPE, UI.WHITE],
        1024: [UI.FRENCHVOILET, UI.WHITE],
        2048: [UI.MEDUIMSTATEBLUE, UI.WHITE],
        4096: [UI.TROPICALVIOLET, UI.WHITE],
        8192: [UI.LAVENDER, UI.WHITE],
        16384: [UI.CHAMPAGNEPINK, UI.GRAY3],
        32768: [UI.SANDYBROWN, UI.WHITE],
        65536: [UI.SANDYBROWN2, UI.WHITE],
        131072: [UI.BURNTSIENNA, UI.WHITE],
        262144: [UI.ENGINEERINGORANGE, UI.WHITE],
        524288: [UI.ROSEWOOD, UI.WHITE],
        1048576: [UI.RICHBLACK, UI.WHITE],
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
                gameBlocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), dic[1048576][0], str(1048576), dic[1048576][1], title_font_link, UI.gameBlockTextResize(1048576), 0.05))
            else:
                gameBlocks.append(UI.Block(pygame.Rect((0.04 + gap_w) * screen_width + j * (block_w + gap_w) * screen_width, (0.3 + gap_h) * screen_height + i * (block_h + gap_h) * screen_height, block_w * screen_width, block_h * screen_height), dic[value][0], str(value), dic[value][1], title_font_link, UI.gameBlockTextResize(value), 0.05))

    # Draw the screen
    screen.fill(UI.PICTONBLUE)
    screen.blit(game_page_background, (0, 0))
    game_title.drawTextWithShadow(screen, UI.AERO, 2)
    quote_text.drawText(screen)

    # Draw the button
    for button in buttons:
        button.drawWithShadow(screen, UI.UNITEDNATIONSBLUE, 3)
    # Draw the score counter block and the history highest score block
    for block in blocks_set[0]:
        block.drawWithShadow(screen, UI.UNITEDNATIONSBLUE, 3)
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

def readRecords():
    # read records
    records = []
    with open('./docs/record/records.json', 'r') as f:
        records = json.load(f)

    # read saves
    save = []
    with open('./docs/save/save01.json', 'r') as f:
        save = json.load(f)

    return records, save

def randomGenerate(save, now):
    if(save['initialized'] == False):
        save['initialized'] = True
        for t in range(2):
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            while now[i][j] == 0:
                i = random.randint(0, 3)
                j = random.randint(0, 3)
            if(t == 0):
                now[i][j] = 2
            else:
                now[i][j] = 4 / random.randint(1, 2)
    else:
        zeros = []
        for i in range(4):
            for j in range(4):
                if now[i][j] == 0:
                    zeros.append([i, j])
        n = len(zeros)
        x = random.randint(0, n - 1)
        i, j = zeros[x]
        now[i][j] = 2
    return now