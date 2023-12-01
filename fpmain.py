# This file was created by: Ben Maya on 11/16/2023
'''Sources:
1. https://github.com/slxmmy999/InfiniteBaseballGrid
2. https://www.immaculategrid.com/basketball/mens
'''

# Title: Immaculate Grid: Countries Edition
'''Goals:
1. Display a 3x3 Grid for Countries
2. Create 20 Random Categories for the Grid
3. Scrape Data for Every Country
'''

import pygame as pg
from fpsettings import *
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.bgimage = pg.image.load(os.path.join(img_folder, 'benmaya_immgrid_bg.png')).convert()
        '''code above is part of what allowed me to get my custom made background into the game
        credit: https://www.askpython.com/python-modules/pygame-looping-background '''
    def show_start_screen(self):
            pass
    def show_go_screen(self):
            pass
    def draw(self):
        self.screen.blit(self.bgimage, (0,0))
        '''drawing the bacckground image I introduced earlier in this code
        credit: https://www.askpython.com/python-modules/pygame-looping-background'''
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        '''these two lines above help display the score'''
        # buffer - after drawing everything, flip display
        pg.display.flip()    
    
g = Game()
while g.running:
    g.new()

pg.quit()