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
        self.all_spirtes = pg.sprite.Group()
        

        self.run()
    '''this code below "runs" the game... all the updates, time, sprites, images''' 
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            # self.update() (not quite using this yet..)
            self.draw()
    
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
        self.draw_text("Has a 'Wonder of the World'", 20, BLACK, 110, 440)
        pg.display.flip()  
    
'''
# Source for creating buttons: https://medium.com/@01one/how-to-create-clickable-button-in-pygame-8dd608d17f1b
    button_surface = pg.Surface((160, 160))
    pg.draw.rect(button_surface, (0, 0, 0),(0, 0, 100, 50))
    # pg.draw.text(button_surface, "Click Me!", (25, 25), (255, 255, 255))

    # Create a pygame.Rect object that represents the button's boundaries
    button_rect = pg.Rect(0, 0, 100, 50)

    # Create a pygame.event.MOUSEBUTTONDOWN event handler that checks if the mouse is clicked inside the button's boundaries
    def on_mouse_button_down(event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and button_rect.collidepoint(event.pos):
            print("Button clicked!")

    button_rect = pg.Rect(0, 0, 100, 50)
    def on_mouse_button_down(event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and button_rect.collidepoint(event.pos):
            print("Button clicked!")
    
    # Call the pygame.display.update() function to display the button on the screen
    pg.display.update()

# Start the main loop
    while True:
    # Get events from the event queue
        for event in pg.event.get():
        # Check for the quit event
         if event.type == pg.QUIT:
            # Quit the game
            pg.quit()
            sys.exit()

        # Check for the mouse button down event
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            on_mouse_button_down(event)

    # Update the game state

    # Draw the game screen
    pygame.display.update()
   '''
    
g = Game()
while g.running:
    g.new()

pg.quit()