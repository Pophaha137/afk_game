import pygame
import sys
import os
import datetime

def get_path():
    return os.getcwd()

def set_char(char, x, y, font_size, color):
    cwd = get_path()
    font = pygame.font.Font(f"{cwd}/VonwaonBitmap-12px.ttf", font_size)
    text = font.render(char, True, color)
    return text, text.get_rect(center=(x, y))

def print_text(screen, text, x, y, font_size, color):
    rendered_text, text_rect = set_char(text, x, y, font_size, color)
    screen.blit(rendered_text, text_rect)