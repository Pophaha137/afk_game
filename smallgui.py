import pygame
import os
import ctypes
import time

from Textbutton import TButton

pygame.init()
def go_Ffloor(screen):
    from Ffloor import FirstFloor
    FirstFloor(screen)
EVENT = pygame.USEREVENT
pygame.time.set_timer(EVENT,1000)
def smallgui(surface):
    running = True
    i= 1
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #synthesis_bar = pygame.transform.scale(pygame.image.load(f"./resource/progress_bar/synthesis/{1}.png").convert_alpha(), (150, 50))
    combatants_bar = pygame.transform.scale(pygame.image.load("./resource/progress_bar/combatant/4.png").convert_alpha(),(150,50))
    forge_bar = pygame.transform.scale(pygame.image.load("./resource/progress_bar/forge/1.png").convert_alpha(),(150,50))
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"), (50, 50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"), (50, 50))
    esc = TButton(0, 0, " ", crossN, crossN, crossD, go_Ffloor, font, (0, 0, 0))
    while running:
        synthesis_bar = pygame.transform.scale(pygame.image.load(f"./resource/progress_bar/synthesis/{i}.png").convert_alpha(), (150, 50))
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx, my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                esc.mouseDown(mx, my)
            elif event.type == pygame.MOUSEBUTTONUP:
                esc.mouseUp(mx, my)
            elif event.type == EVENT:
                if i < 7:
                    i =i+1
        screen.fill((255,255,255))
        screen.blit(combatants_bar,(50,0))
        screen.blit(synthesis_bar,(50,50))
        screen.blit(forge_bar,(50,100))
        esc.draw(screen)
        pygame.display.flip()

    pygame.quit()


user_screen = ctypes.windll.user32
screensize = user_screen.GetSystemMetrics(0), user_screen.GetSystemMetrics(1)
x = screensize[0]-200
y = screensize[1]-200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d"%(x,y)
screen = pygame.display.set_mode((200,150),pygame.NOFRAME)
if __name__ == '__main__':
    smallgui(screen)