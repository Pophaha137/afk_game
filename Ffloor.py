import pygame
import sys
from Textbutton import TButton
from function import *
from character import *
from character_func import load_player,save_player
pygame.init()
EVENT1 = pygame.USEREVENT
pygame.time.set_timer(EVENT1, 1000)
player = load_player()
def go_gui(screen):
    from smallgui import smallgui
    smallgui(screen)
def go_fight(screen):
    global player
    generate_enemy(0,1)
    generate_enemy(1,2)
    generate_enemy(2,3)
    generate_enemy(3,3)
    generate_enemy(4,3)
    fight(player,enemy[0])
    return screen
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
    small_font = pygame.font.Font("./VonwaonBitmap-12px.ttf",20)
    #image import
    cruciblei = pygame.transform.scale(pygame.image.load("./resource/function/AlchemyPot.png").convert_alpha(),(200,200))
    forgei = pygame.transform.scale(pygame.image.load("./resource/function/Blacksmith.png").convert_alpha(),(200,200))
    bloodi = pygame.transform.scale(pygame.image.load("./resource/character/blood.png").convert_alpha(),(200,100))
    headi = pygame.transform.scale(pygame.image.load("./resource/character/backpack.png").convert_alpha(),(150,150))
    doori = pygame.transform.scale(pygame.image.load("./resource/character/AdventureDoor.png").convert_alpha(),(200,200))
    stairsi = pygame.transform.scale(pygame.image.load("./resource/character/stair.png").convert_alpha(),(150,200))
    bExitD = pygame.transform.scale(pygame.image.load("./resource/background/bExitD.png").convert_alpha(),(150,50))
    bExitM = pygame.transform.scale(pygame.image.load("./resource/background/bExitM.png").convert_alpha(),(150,50))
    bExitN = pygame.transform.scale(pygame.image.load("./resource/background/bExitN.png").convert_alpha(),(150,50))
    #button
    crucible = TButton(0, 100," ", cruciblei, cruciblei, None,synthesis, font,(0,0,0))
    forge = TButton(w/3*2, 0," ", forgei, forgei, None, smithy, font, (0,0,0))
    head = TButton(0, h-150," ", headi, headi, None, backpack, font, (0,0,0))
    door = TButton(500, h-200, " ", doori, doori, None, go_fight,font, (0,0,0))
    stairs = TButton(w-150, h-200, " ", stairsi, stairsi, None, SecondFloor,font, (0,0,0))
    go_to_gui = TButton(w-350, h-50, "Small", bExitN, bExitM,bExitD,go_gui,small_font, (255,255,255))

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
                go_to_gui.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    crucible.mouseDown(mx,my)
                    forge.mouseDown(mx,my)
                    head.mouseDown(mx,my)
                    door.mouseDown(mx,my)
                    stairs.mouseDown(mx,my)
                    go_to_gui.mouseDown(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                crucible.mouseUp(mx,my)
                forge.mouseUp(mx,my)
                head.mouseUp(mx,my)
                door.mouseUp(mx,my)
                stairs.mouseUp(mx,my)
                go_to_gui.mouseUp(mx,my)
            elif event.type == EVENT1:
                pygame.display.update()
            surface.fill((255,255,255))
            crucible.draw(surface)
            forge.draw(surface)
            head.draw(surface)
            door.draw(surface)
            stairs.draw(surface)
            go_to_gui.draw(surface)
            surface.blit(bloodi,(100,h-100))
        pygame.display.flip()

screen = pygame.display.set_mode((1280, 800))
if __name__ == '__main__':

    FirstFloor(screen)