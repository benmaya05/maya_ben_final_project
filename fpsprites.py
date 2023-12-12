# This file was created by: Ben Maya on 12/1/2023

import pygame as pg
from pygame.sprite import Sprite
import os
from fpsettings import *

# https://www.britannica.com/topic/list-of-countries-1993160

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
            "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
            "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados",
            "Belarus", "Belgium", "Belize", "Benin", "Bhutan"
            "Bolivia", "Bosnia and Herzegovina", "Bostwana", "Brazil", "Brunei"
            "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
            "Cameroon", "Canada", "Central African Republic", "Chad", "Chile",
            "China", "Colombia", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo",
            "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus",
            "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
            "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
            "Finland", "France", "Gabon", "The Gambia", "Georgia",
            "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
            "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
            "Hungary", "Iceland", "India", "Indonesia", "Iran",
            "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
            "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
            "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan",
            "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
            "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
            "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
            "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
            "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
            "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
            "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
            "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
            "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
            "Poland", "Portugal", "Qatar", "Romania", "Russia",
            "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
            "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
            "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
            "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka",
            "Sudan", "South Sudan", "Suriname", "Sweden", "Switzerland",
            "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
            "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
            "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
            "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
            "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia",
            "Zimbabwe"
             ]

# Platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        '''category can be either moving or normal'''
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.index = 0
        '''self.image = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_lavaplat.png')).convert()
        originally where I tried to import my custom platform image... but this ruined the groun platform'''
        # https://www.pygame.org/docs/ref/font.html used this for everything below
        self.image.fill(WHITE)
        FONT = pg.font.SysFont('Arial', 20)
        textsurface = FONT.render(countries[self.index], True, BLACK)
        self.image.blit(textsurface,(0,0))
        #self.image.set_alpha(0)
        
        # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_colorkey helped me make it transparent!!
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
      
# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            if(self.x <= mouse[0] <= self.x+self.w and self.y <= mouse[1] <=self.y+self.h):
                self.index+=1
                self.image = pg.Surface((self.w, self.h))
                self.image.fill(WHITE)
                FONT = pg.font.SysFont('Arial', 20)
                textsurface = FONT.render(countries[self.index], True, BLACK)
                self.image.blit(textsurface,(0,0))
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
                print(countries[self.index])

        
        
