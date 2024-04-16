import pygame
import sys
from Textbutton import TButton
from function import *
def FirstFloor(surface):
    global state
    from backpack import backpack
    from smithy import smithy
    from Sfloor import SecondFloor
    from synthesis import synthesis
    state = "Floor"
    #screen size
    w=1280
    h=800
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #image import
    cruciblei = pygame.transform.scale(pygame.image.load("./resource/function/crucible.png").convert_alpha(),(200,200))
    forgei = pygame.transform.scale(pygame.image.load("./resource/function/forge.png").convert_alpha(),(200,200))
    bloodi = pygame.transform.scale(pygame.image.load("./resource/character/blood.png").convert_alpha(),(200,100))
    headi = pygame.transform.scale(pygame.image.load("./resource/character/head.png").convert_alpha(),(100,150))
    doori = pygame.transform.scale(pygame.image.load("./resource/character/door.png").convert_alpha(),(100,200))
    stairsi = pygame.transform.scale(pygame.image.load("./resource/character/stairs.png").convert_alpha(),(150,200))

    #button
    crucible = TButton(0, 100," ", cruciblei, cruciblei, None,synthesis, font,(0,0,0))
    forge = TButton(w/3*2, 0," ", forgei, forgei, None, smithy, font, (0,0,0))
    head = TButton(0, h-150," ", headi, headi, None, backpack, font, (0,0,0))
    door = TButton(500, h-200, " ", doori, doori, None, None,font, (0,0,0))
    stairs = TButton(w-150, h-200, " ", stairsi, stairsi, None, SecondFloor,font, (0,0,0))

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                crucible.getFocus(mx,my)
                forge.getFocus(mx,my)
                head.getFocus(mx,my)
                door.getFocus(mx,my)
                stairs.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    crucible.mouseDown(mx,my)
                    forge.mouseDown(mx,my)
                    head.mouseDown(mx,my)
                    door.mouseDown(mx,my)
                    stairs.mouseDown(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                crucible.mouseUp(mx,my)
                forge.mouseUp(mx,my)
                head.mouseUp(mx,my)
                door.mouseUp(mx,my)
                stairs.mouseUp(mx,my)
            surface.fill((255,255,255))
            crucible.draw(surface)
            forge.draw(surface)
            head.draw(surface)
            door.draw(surface)
            stairs.draw(surface)
            surface.blit(bloodi,(100,h-100))
        pygame.display.flip()

screen = pygame.display.set_mode((1280, 800))
if __name__ == '__main__':

    FirstfFloor(screen)