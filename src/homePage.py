import pygame, sys
from pygame.locals import *
import tools.UI as UI
import random

# basic setting
screen_width = 400
screen_height = 600
title_font_link = './docs/asset/font/Roboto-Bold.ttf'
open_title = UI.Text(title_font_link, 100, '2048', UI.WHITE, 0.5 * screen_width, 0.2 * screen_height)

def homePageBackground():
    home_page_background = pygame.image.load('./docs/asset/image/home_page_background.png')
    home_page_background = pygame.transform.scale(home_page_background, (screen_width, screen_height))
    home_page_background.convert()
    return home_page_background

def homeButtonSetting():
    buttons = []
    buttons.append(UI.Button(pygame.Rect(0.2 * screen_width, 0.45 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UI.UNITEDNATIONSBLUE, 'START', UI.WHITE, title_font_link, 35, '0to1'))
    buttons.append(UI.Button(pygame.Rect(0.2 * screen_width, 0.575 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UI.UNITEDNATIONSBLUE, 'SETTING', UI.WHITE, title_font_link, 35, '0to2'))
    buttons.append(UI.Button(pygame.Rect(0.2 * screen_width, 0.7 * screen_height, 0.6 * screen_width, 0.1 * screen_height), UI.UNITEDNATIONSBLUE, 'ABOUTUS', UI.WHITE, title_font_link, 35, '0to3'))
    return buttons

def homePage(screen, buttons):
    # image
    home_page_background = homePageBackground()
    # Draw the screen
    screen.fill(UI.TURQUOISE)
    screen.blit(home_page_background, (0, 0))
    # screen.blit(title_shadow_surface, title_shadow_rect)
    open_title.drawTextWithShadow(screen, UI.AERO, 2)
    # Draw the button
    for button in buttons:
        button.drawWithShadow(screen, UI.SLATEBLUE, 3)