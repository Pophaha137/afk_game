import pygame
import sys
import os
from function import *
from lib import *
from button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adventurer Simulator")
#image import
stbtnN - pygame.image,load("./resources/")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
       # elif event.type == pygame.MOUSEMOTION:


    screen.fill((255, 255, 255))
    print_text(screen, "AFK Game", 400, 175, 50, (0, 0, 0))
    print_text(screen, "Dumb ass pophaha137", 400, 350, 20, (0, 0, 0))
    pygame.display.flip()