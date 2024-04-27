import pygame
import sys
import os
import datetime
import pickle

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

# 将数据保存到文件中
def save_items_to_file(filename, items):
    directory = 'data'
    if filename == "weapons.pkl" or filename == "armors.pkl" or filename == "jewelrys.pkl" or filename == "item_list.pkl":
        for i in items:
            i.img = None
    file = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 将数据保存到文件中
    with open(file, 'wb') as f:
        pickle.dump(items, f)
    # print(f"Items saved to {file}.")
    items = load_items_from_file(filename)

    # 从文件中加载数据


def load_items_from_file(filename):
    items = []
    directory = 'data'
    file = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 如果文件存在则加载数据
    if os.path.exists(file):
        with open(file, 'rb') as f:
            items = pickle.load(f)
        # print(f"Items loaded from {filename}.")
        return items
    # 如果文件不存在则创建一个新文件
    else:
        print(f"File {filename} does not exist. Creating a new file.")
        with open(file, 'wb') as f:
            pickle.dump(items, f)
        print(f"New file {file} created.")
        return items
