import pygame
import sys
from Textbutton import TButton
from function import *
def FirstfFloor(surface):
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #image import
    cruciblei = pygame.transform.scale(pygame.image.load("./resource/function/crucible.png").convert_alpha(),(200,200))
    forgei = pygame.transform.scale(pygame.image.load("./resource/function/forge.png").convert_alpha(),(200,200))
    bloodi = pygame.transform.scale(pygame.image.load("./resource/character/blood.png").convert_alpha(),(200,100))
    headi = pygame.transform.scale(pygame.image.load("./resource/character/head.png").convert_alpha(),(100,150))
    doori = pygame.transform.scale(pygame.image.load("./resource/character/door.png").convert_alpha(),(100,200))
    stairsi = pygame.transform.scale(pygame.image.load("./resource/character/stairs.png").convert_alpha(),(150,200))

    #button
    crucible = TButton(0, 100," ", cruciblei, cruciblei, None,None, font,(0,0,0))
    forge = TButton(400, 0," ", forgei, forgei, None, None, font, (0,0,0))
    head = TButton(0, 450," ", headi, headi, None, None, font, (0,0,0))
    door = TButton(500, 400, " ", doori, doori, None, None,font, (0,0,0))
    stairs = TButton(650, 400, " ", stairsi, stairsi, None, None,font, (0,0,0))

    #main
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
                if pygame.mouse.get_pressed()[0]:
                    crucible.mouseDown(mx,my)
                    forge.mouseDown(mx,my)
                    head.mouseDown(mx,my)
                    door.mouseDown(mx,my)
                    stairs.mouseDown(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                crucible.mouseUp(mx,my)
                forge.mouseUp(mx,my)
                head.mouseDown(mx,my)
                door.mouseDown(mx,my)
                stairs.mouseDown(mx,my)
            surface.fill((255,255,255))
            crucible.draw(surface)
            forge.draw(surface)
            head.draw(surface)
            door.draw(surface)
            stairs.draw(surface)
            surface.blit(bloodi,(100,500))
        pygame.display.flip()