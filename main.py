import pygame, sys
from UI import colors
from pygame.locals import *

# color
WHITE = colors.hex_to_rgb('#FFFFFF')
BLACK = colors.hex_to_rgb('#000000')
GRAY = colors.hex_to_rgb('#574D4D')
BLUE1 = colors.hex_to_rgb('#73C6D9')
BLUE2 = colors.hex_to_rgb('#5EA3A3')
BLUE3 = colors.hex_to_rgb('#3A656A')
BLUE4 = colors.hex_to_rgb('#2E4E50')
BEIGE = colors.hex_to_rgb('#F2EBDC') # 米黃色

# screen setting
screen_width = 400
screen_height = 600

# link
title_font_link = './Assets/font/Poppins-Medium.ttf'

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('2048')

# draw text
font_obj = pygame.font.Font(title_font_link, 32) #創字體的物件
title_surface = font_obj.render('2048 GAME', True, BLACK) #創文字Surface
title_rect = title_surface.get_rect() #文字方塊
title_rect.center = (0.5 * screen_width, 0.2 * screen_height)

while True:
    # Event handing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the screen
    screen.fill(BEIGE)
    screen.blit(title_surface, title_rect)

    # Update the screen
    pygame.display.update()
