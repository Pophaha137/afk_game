import pygame
from equipment import *
from class_define import *

forge_img = []
def forge_img_generate():
    for i in sword_name:
        img = pygame.image.load("resource/weapon/" + str(i) + ".png")
        img = pygame.transform.scale(img, (44, 48))
        forge_img.append(img)
        """
    for i in armor_name:
        img = pygame.image.load("resource/armor/" + str(i) + ".png")
        img = pygame.transform.scale(img, (44, 48))
        forge_img.append(img)
        """


item_img = []
def item_img_generate():
    global item_name
    for i in item_name:
        img = pygame.image.load("resource/item/" + str(i) + ".png")
        img = pygame.transform.scale(img, (50, 50))
        item_img.append(img)

forge_img_generate()
item_img_generate()

#def print_img(surface, page=0):

