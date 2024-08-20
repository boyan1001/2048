import pygame, sys
from pygame.locals import *
import tools.UI as UI
import src.gamePage as game
import src.homePage as home
import random
import json

# Colors
# UI.WHITE = UI.hexToRgb('#FFFFFF')
# UI.BLACK = UI.hexToRgb('#000000')
# UI.GRAY = UI.hexToRgb('#F2F2F2')
# UI.GRAY2 = UI.hexToRgb('#E3E3E3')
# UI.BLUE1 = UI.hexToRgb('#73C6D9')
# UI.BLUE2 = UI.hexToRgb('#5EA3A3')
# UI.BLUE3 = UI.hexToRgb('#3A656A')
# UI.BLUE4 = UI.hexToRgb('#2E4E50')
# UI.BLUE5 = UI.hexToRgb('#AAEBFF')
# UI.BEIGE = UI.hexToRgb('#F2EBDC') # 米黃色
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
# UI.GRAY3 = UI.hexToRgb('#918085') # 香檳粉
# UI.GRAY4 = UI.hexToRgb('#438572') # 灰色4


# Screen setting
FPS = 60
screen_width = 400
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')
now_page_value = 0
prev_page_value = -1
temp_rd = []
temp_sv = []
now = [[0 for i in range(4)] for j in range(4)]
buttons = [] # Button setting
title_font_link = './docs/asset/font/Roboto-Bold.ttf' # Font

while True:
    # Set the frame rate
    clock.tick(FPS)

    if(prev_page_value != now_page_value):
        if(now_page_value == 0):
            buttons = home.homeButtonSetting()
        elif(now_page_value == 1):
            buttons = game.gameButtonSetting()

    # Update the value
    prev_page_value = now_page_value
    
    # Event handing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # judge your mouse on the button or not
        x, y = pygame.mouse.get_pos()
        for button in buttons:
            button.clickJudge(x, y)
        # click the button
        if event.type == MOUSEBUTTONDOWN:
            for button in buttons:
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
        home.homePage(screen, buttons)
    elif(now_page_value == 1):
        # read records and saves
        if(prev_page_value != now_page_value):
            temp_rd, temp_sv = game.readRecords()
            now = temp_sv['board']
            if(temp_sv['initialized'] == False):
                game.randomGenerate(temp_sv, now)
                temp_sv['initialized'] = True
        game.gamePage(temp_rd, temp_sv, screen, buttons, now)
        game.writeRecords(temp_rd, temp_sv, now)

    # Update the screen
    pygame.display.update()
