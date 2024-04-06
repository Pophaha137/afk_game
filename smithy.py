import pygame
from Textbutton import TButton
from function import *

def smithy(surface):
    from Ffloor import FirstfFloor
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"),(50,50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"),(50,50))
    smithy = pygame.transform.scale(pygame.image.load("./resource/character/TUI.png"),(1280,800))
    #button
    esc = TButton(1230,0, " ", crossN, crossN,crossD,FirstfFloor, font,(0,0,0))
    running = True
    while running:
        for event in pygame.event.get():
            mx,my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    esc.mouseDown(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                esc.mouseUp(mx,my)
            surface.blit(smithy,(0,0))
            esc.draw(screen)
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1280, 800))
if __name__ == '__main__':
    smithy(screen)
