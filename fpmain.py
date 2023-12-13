# This file was created by: Ben Maya on 11/16/2023
'''Sources:
1. https://github.com/slxmmy999/InfiniteBaseballGrid
2. https://www.immaculategrid.com/basketball/mens

code from Chris Bradfield's tutorials
content from kids can code: http://kidscancode.org/blog/
https://github.com/kidscancode/pygame_tutorials/tree/master/platform
'''

# Title: Immaculate Grid: Countries Edition
'''Goals:
1. Display a 3x3 Grid for Countries
2. Create 20 Random Categories for the Grid
3. Scrape Data for Every Country
'''

import pygame as pg
from pygame.sprite import Sprite
from fpsettings import *
from fpsprites import *
import os
import random
import sys

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
        self.bgimage = pg.image.load(os.path.join(img_folder, 'benmaya_3x3gridfinal.png')).convert()
        '''code above is part of what allowed me to get my custom made background into the game
        credit: https://www.askpython.com/python-modules/pygame-looping-background '''
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        

        self.run()
    '''this code below "runs" the game... all the updates, time, sprites, images''' 
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            # self.update() (not quite using this yet..)
            self.draw()

    def update(self):
        self.all_sprites.update()
    
    def draw_text(self, text, size, color, x, y):
            font_name = pg.font.match_font('arial')
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            self.screen.blit(text_surface, text_rect)

    # def update(self):
        
    def events(self):
        for event in pg.event.get():
            for sprites in self.all_sprites:
                 sprites.update(event)
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def show_start_screen(self):
            pass
    def show_go_screen(self):
            pass
    def draw(self):
        self.screen.blit(self.bgimage, (0,0))
        '''drawing the bacckground image I introduced earlier in this code
        credit: https://www.askpython.com/python-modules/pygame-looping-background'''    
        # buffer - after drawing everything, flip display
        self.draw_text("Country in Africa", 20, BLACK, 300, 6)
        self.draw_text("World Cup Winner", 20, BLACK, 465, 6)
        self.draw_text("Island Nation", 20, BLACK, 630, 6)
        self.draw_text("Red in Flag", 20, BLACK, 160, 110)
        self.draw_text("English is an Official Language", 19, BLACK, 110, 270)
        self.draw_text("Has a Nobel Peace Prize Winner", 18, BLACK, 110, 440)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

  
    
g = Game()
while g.running:
    g.new()

pg.quit()