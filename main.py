import pygame
import sys
import os
from function import *
from lib import *
from Textbutton import TButton
from Ffloor import FirstfFloor

#screen size
w=1280
h=800
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Adventurer Simulator")
#state
current_state = "surface"
#font
font = pygame.font.Font("./VonwaonBitmap-12px.ttf",80)
def Surface(surface):
    global w,h
    #Text
    surTitle = font.render("Adventurer Simulator",True,(0,0,0))
    #image import
    stbtnN = pygame.transform.scale(pygame.image.load("./resource/background/button/stBtnN.png").convert_alpha(),(200,50))
    stbtnD = pygame.transform.scale(pygame.image.load("./resource/background/button/stBtnD.png").convert_alpha(),(200,50))
    #button
    stbtn = TButton(w/2-100, h/5*3, " ", stbtnN, stbtnD, None, FirstfFloor, font, (0,0,0))
    running = True
    while running:
        for event in pygame.event.get():
            mx,my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            if current_state == "surface":
                if event.type == pygame.MOUSEMOTION:
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
    Surface(screen)