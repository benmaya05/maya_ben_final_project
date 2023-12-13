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
            "China", "Colombia", "Comoros", "DR Congo", "Republic of the Congo",
            "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus",
            "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
            "East Timor", "Ecuador", "Egypt", "El Salvador", "England", "Equatorial Guinea",
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

# here are the possible answers:
'''
Box 1: Algeria, Angola, Benin, Burkina Faso, Burundi, 
        Cameroon, Central African Republic, Cape Verde, Chad, Comoros, 
        DR Congo, Republic of Congo, Djibouti, Egypt, Equatorial Guinea, 
        Eritrea, Eswatini, Ethiopia, Gambia, Ghana, 
        Guinea, Guinea-Bissau, Kenya, Liberia, Libya, 
        Madagascar, Mali, Malawi, Mauritania, Mauritius, 
        Morocco, Mozambique, Namibia, Sao Tome and Principe, Senegal, 
        Seychelles, South Africa, Sudan, South Sudan, Togo, 
        Tunisia, Uganda, Zambia, Zimbabwe

Box 2: England, France, Germany, Italy, Spain

Box 3: Antigua and Barbuda, Bahrain, Brunei, Cape Verde, Comoros, 
        Cuba, Dominica, Dominican Republic, East Timor, Fiji, 
        Grenada, Haiti, Iceland, Indonesia, Japan, 
        Kiribati, Madagascar, Maldives, Malta, Mauritius, 
        New Zealand, Papua New Guinea, Philippines, Saint Kitts and Nevis, Samoa, 
        Sao Tome and Principe, Seychelles, Singapore, Sri Lanka, Tonga, 
        Trinidad and Tobago, Tuvalu, United Kingdom, Vanuatu, Taiwan

Box 4: Botswana, Burundi, Cameroon, Eswatini, Gambia, 
        Ghana, Kenya, Lesotho, Liberia, Malawi, 
        Namibia, Nigeria, Rwanda, Seychelles, Sierra Leone, 
        South Africa, Sudan, South Sudan, Tanzania, Uganda, 
        Zambia, Zimbabwe

Box 5: England

Box 6: Antigua and Barbuda, Australia, Bahamas, Barbados, Dominica, 
        Fiji, Grenada, Ireland, Jamaica, Kiribati, 
        Marshall Islands, Micronesia, Nauru, New Zealand, Palau, 
        Papua New Guinea, Philippines, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, 
        Samoa, Seychelles, Solomon Islands, Tonga, Trinidad and Tobago, 
        Tuvalu, Vanuatu

Box 7: DR Congo, Egypt, Ethiopia, Ghana, Kenya, 
        Liberia, South Africa, Tunisia,

Box 8: Argentina, France, Germany, Italy

Box 9: Ireland, Japan, Philippines
'''

# Platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.index = 0
        # https://www.pygame.org/docs/ref/font.html used this for everything below
        self.image.fill(WHITE)
        FONT = pg.font.SysFont('Arial', 20)
        textsurface = FONT.render(countries[self.index], True, BLACK)
        self.image.blit(textsurface,(0,0))

        
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

        
        
