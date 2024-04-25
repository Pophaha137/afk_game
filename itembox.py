import pygame
import json
from Textbutton import TButton
from function import *
from equipment import *
from class_define import *


def print_img(surface, print_page, page=0):
    items_per_page = 30  # 每页的物品数量
    items_per_row = 6  # 每行的物品数量
    start_index = items_per_page * page  # 开始的索引
    end_index = start_index + items_per_page  # 结束的索引

    items = load_items_from_file("item_list.pkl")
    img_list = items[start_index:end_index]

    x = 368  # 初始x坐标
    y = 38  # 初始y坐标
    count = 0  # 当前行的物品数量
    for item in img_list:
        img = item.get_img()  # 获取物品图片
        surface.blit(img, (x, y))  # 将图片绘制到surface上
        x += img.get_width() + 8  # 更新x坐标以便下一个图片不会覆盖当前图片
        count += 1  # 更新当前行的物品数量
        if count == items_per_row:  # 如果当前行的物品数量达到了6，就换行
            x = 368  # 重置x坐标
            y += img.get_height()   # 更新y坐标以便下一个图片在新的一行
            count = 0  # 重置当前行的物品数量


def position_id(mx, my):
    x = 368
    y = 38
    count = 0
    for i in range(30):
        if x < mx < x + 98 and y < my < y + 107:
            #print (i)
            return i
        x += 98
        count += 1
        if count == 6:
            x = 368
            y += 107
            count = 0
    # print(-1)
    return -1

def print_num(surface):
    for i in range(30):
        x = 430
        y = 120
        count = 0
        item = load_items_from_file("item_list.pkl")
        for i in item:
            print_text(surface, str(i.show_number()) , x, y, 25, (255,255,255))
            x += 100
            count += 1
            if count == 6:
                x = 368
                y += 107
                count = 0

def print_text(surface, text, x, y, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)  # 设置文本矩形的左上角坐标
    surface.blit(text_surface, text_rect)


def print_title(surface):
    x = 45
    y = 100
    size = 40
    print_text(surface, "Items", x, y, size, (0, 0, 0))


def print_info(surface, page, position_id):
    size = 26
    x = 45
    y = 150
    if position_id != -1:
        i = position_id + page * 30
        items = load_items_from_file("item_list.pkl")
        if i < len(items):
            item = items[i]
            text_dict = item.to_dict()

            for key, value in text_dict.items():
                text = f"{key}: {value}"
                print_text(surface, text, x, y, size, (0, 0, 0))
                y += 20  # 更新y坐标以便下一个文本在新的一行
def chest(surface):
    mx, my = 0, 0
    page = 0
    from Sfloor import SecondFloor
    # 时钟
    clock = pygame.time.Clock()
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    page_font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 24)
    # image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"), (50, 50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"), (50, 50))
    pakage = pygame.transform.scale(pygame.image.load("./resource/character/inventory.png"), (1080, 600))

    # 背包物品展示
    select_position_id = -1  # 选中的物品的索引
    print_page = 0  # 当前选择页数

    # button
    esc = TButton(1230, 0, " ", crossN, crossN, crossD, SecondFloor, font, (0, 0, 0))
    running = True

    while running:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            position_id(mx, my)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx, my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    esc.mouseDown(mx, my)
                    if 500 < mx < 600 and 600 < my < 700:
                        if page >= 1:
                            page -= 1

                    elif 600 < mx < 700 and 600 < my < 700:
                        if page <= 18:
                            page += 1
                    elif 900 < mx < 1000 and 600 < my < 700:
                        if print_page != 0:
                            print_page -= 1
                            page = 0

                    elif 1000 < mx < 1100 and 600 < my < 700:
                        print_page += 1
                        if print_page == 3:
                            print_page = 0
                            page = 0

                    else:
                        generate_weapon(0, 10)
            elif event.type == pygame.MOUSEBUTTONUP:
                esc.mouseUp(mx, my)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 600, 100, 100), 2)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(600, 600, 100, 100), 2)


        surface.blit(pakage, (0, 0))

        rect_x, rect_y, rect_width, rect_height = 350, 600, 100, 50
        pygame.draw.rect(surface, (196, 164, 132), [rect_x, rect_y, rect_width, rect_height])
        page_num_text = page_font.render(f'Page {page}', True, (255, 255, 255))
        text_rect = page_num_text.get_rect(center=(rect_x + rect_width / 2, rect_y + rect_height / 2))
        surface.blit(page_num_text, text_rect)

        esc.draw(screen)
        print_img(screen, print_page, page)
        print_title(screen)
        print_info(screen, page, position_id(mx, my))
        print_num(screen)
        pygame.display.flip()
        clock.tick(120)


pygame.init()
screen = pygame.display.set_mode((1280, 800))

if __name__ == '__main__':
    chest(screen)