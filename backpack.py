import pygame
from Textbutton import TButton
from function import *

pygame.init()
display = pygame.display.set_mode((800, 600), pygame.NOFRAME)
Run = True


def font(text, position, color=(255, 255, 255)):
    Font = pygame.font.Font("VonwaonBitmap-12px.ttf", 30).render(text, True, color)
    FontRect = Font.get_rect()
    FontRect.center = position
    display.blit(Font, FontRect)
    return FontRect


if __name__ == '__main__':
    while Run:
        font("无边框窗体实例", [400, 300])