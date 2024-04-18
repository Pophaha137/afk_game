import pygame
import sys
from Textbutton import TButton
from function import *
def SecondFloor(surface):
    global state
    from backpack import backpack
    #from itembox import itembox
    from Ffloor import FirstFloor
    state = "Sfloor"
    #screen size
    w=1280
    h=800
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #image import
    bloodi = pygame.transform.scale(pygame.image.load("./resource/character/blood.png").convert_alpha(),(200,100))
    headi = pygame.transform.scale(pygame.image.load("./resource/character/backpack.png").convert_alpha(),(100,150))
    boxi = pygame.transform.scale(pygame.image.load("./resource/function/chest.png").convert_alpha(),(200,200))
    stairsi = pygame.transform.scale(pygame.image.load("./resource/character/stair.png").convert_alpha(),(150,200))

    #button
    head = TButton(0, h-150," ", headi, headi, None, backpack, font, (0,0,0))
    box = TButton(500, 0, " ", boxi, boxi, None, None,font, (0,0,0))
    stairs = TButton(w-150, 0, " ", stairsi, stairsi, None, FirstFloor,font, (0,0,0))

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                head.getFocus(mx,my)
                box.getFocus(mx,my)
                stairs.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    head.mouseDown(mx,my)
                    box.mouseDown(mx,my)
                    stairs.mouseDown(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                head.mouseUp(mx,my)
                box.mouseUp(mx,my)
                stairs.mouseUp(mx,my)
            surface.fill((255,255,255))
            head.draw(surface)
            box.draw(surface)
            stairs.draw(surface)
            surface.blit(bloodi,(100,h-100))
        pygame.display.flip()

screen = pygame.display.set_mode((1280, 800))
if __name__ == '__main__':
    SecondFloor(screen)