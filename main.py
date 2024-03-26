import pygame
import sys
import os
from lib import *
from button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AFK Game")


running = True
while running != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    print_text(screen, "AFK Game", 400, 300, 50, (0, 0, 0))
    pygame.display.flip()