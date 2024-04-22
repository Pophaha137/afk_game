import pygame
import sys
import os
from function import *
from lib import *
from backpack import *
from equipment import *
from Textbutton import TButton
from Ffloor import FirstFloor
#screen size
w=1280
h=800
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Adventurer Simulator")
#font
font = pygame.font.Font("./VonwaonBitmap-12px.ttf",80)
def Surface(surface):
    global w,h,state
    state = "start"
    #Text
    surTitle = font.render("Adventurer Simulator",True,(0,0,0))
    #image import
    stbtnN = pygame.transform.scale(pygame.image.load("./resource/background/button/stBtnN.png").convert_alpha(),(200,50))
    stbtnD = pygame.transform.scale(pygame.image.load("./resource/background/button/stBtnD.png").convert_alpha(),(200,50))
    #button
    stbtn = TButton(w/2-100, h/5*3, " ", stbtnN, stbtnD, None, FirstFloor, font, (0,0,0))
    running = True
    while running:
        for event in pygame.event.get():
            mx,my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                stbtn.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()==(1,0,0):
                        stbtn.mouseDown(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                stbtn.mouseUp(mx,my)
            screen.fill((255, 255, 255))
            stbtn.draw(screen)
            surface.blit(surTitle,(w/2-surTitle.get_width()/2,h/3))

        pygame.display.flip()

if __name__ == '__main__':
    weapons =       load_items_from_file("weapons.pkl")
    weapon_hash =   load_items_from_file("weapon_hash.pkl")
    armors =        load_items_from_file("armors.pkl")
    armor_hash =    load_items_from_file("armor_hash.pkl")
    jewelrys =      load_items_from_file("jewelrys.pkl")
    jewelry_hash =  load_items_from_file("jewelry_hash.pkl")
    Surface(screen)