import pygame
from equipment import *
from class_define import *

forge_img = []
def forge_img_generate():
    for i in len(sword_name):
        img = pygame.image.load("img/sword/" + str(i) + ".png")
        forge_img.append(img)
    for i in len(armor_name):
        img = pygame.image.load("img/armor/" + str(i) + ".png")
        forge_img.append(img)
    for i in len(jewelry_name):
        img = pygame.image.load("img/jewelry/" + str(i) + ".png")
        forge_img.append(img)

item_list = generate_item()
item_img = []
def item_img_generate():
    global item_list
    for i in len(item_list):
        img = pygame.image.load("img/item/" + str(i) + ".png")
        item_img.append(img)

#def print_img(surface, page=0):

