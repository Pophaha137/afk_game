import pygame
from Textbutton import TButton
from function import *



def backpack(surface):
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
    #image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"),(50,50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"),(50,50))
    #button
    esc = TButton(750,0, " ", crossN, crossN,crossD,terminate, font,(0,0,0))
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
            surface.fill((255,255,255))
            esc.draw(screen)
        pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
if __name__ == '__main__':
    backpack(screen)