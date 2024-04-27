import pygame
from Textbutton import TButton
from function import *

def smithy(surface):
    from Ffloor import FirstFloor
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"),(50,50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"),(50,50))
    smithy = pygame.transform.scale(pygame.image.load("./resource/background/equip_background.png"),(1500,1000))
    equip_background = pygame.transform.scale(pygame.image.load("./resource/background/equip_background.png"),(1000,1400))
    reforging_background = pygame.transform.scale(pygame.image.load("./resource/background/button/block.png"),(600,600))
    forge = pygame.transform.scale(pygame.image.load("./resource/character/forge.png"), (300, 300))
    first_item_display = pygame.transform.scale(pygame.image.load("./resource/background/button/item_display.png"),(90,90))
    second_item_display = pygame.transform.scale(pygame.image.load("./resource/background/button/item_display.png"),(90,90))
    result_display = pygame.transform.scale(pygame.image.load("./resource/background/button/item_display.png"),(90,90))
    add_button = pygame.transform.scale(pygame.image.load("./resource/background/button/add.png"),(60,60))
    equal_button = pygame.transform.scale(pygame.image.load("./resource/background/button/equal.png"), (60,60))
    item_slot = pygame.transform.scale(pygame.image.load("./resource/background/button/item_slot.png"),(60,60))

    rows, columns = 6, 4
    slot_width, slot_height = 90, 90
    slot_margin = 10  # Margin between slots
    start_x, start_y = 800, 10  # Starting position of the grid

    #button
    esc = TButton(1230,0, " ", crossN, crossN,crossD,FirstFloor, font,(0,0,0))
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
            surface.blit(smithy,(-400,-200))
            surface.blit(equip_background,(600,-200))
            surface.blit(reforging_background,(0,400))
            surface.blit(first_item_display,(30,600))
            surface.blit(second_item_display, (240, 600))
            surface.blit(result_display,(480,600))
            surface.blit(add_button,(150,615))
            surface.blit(equal_button,(380,615))
            surface.blit(forge, (150, 100))

            for row in range(rows):
                for column in range(columns):
                    slot_x = start_x + column * (slot_width + slot_margin)
                    slot_y = start_y + row * (slot_height + slot_margin)
                    surface.blit(item_slot, (slot_x, slot_y))
            esc.draw(screen)
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1280, 800))
if __name__ == '__main__':
    smithy(screen)
