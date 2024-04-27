import pygame
import json
from Textbutton import TButton
from function import *
from equipment import *



def print_img(surface, print_page, page=0):
    items_per_page = 30  # 每页的物品数量
    items_per_row = 6  # 每行的物品数量
    start_index = items_per_page * page  # 开始的索引
    end_index = start_index + items_per_page  # 结束的索引

    if print_page == 0:
        weapons = load_items_from_file("weapons.pkl")
        img_list = weapons[start_index:end_index]  # 获取当前页的物品
    elif print_page == 1:
        armors = load_items_from_file("armors.pkl")
        img_list = armors[start_index:end_index]
    elif print_page == 2:
        jewelrys = load_items_from_file("jewelrys.pkl")
        img_list = jewelrys[start_index:end_index]
    else:
        print_page = 0

    x = 368  # 初始x坐标
    y = 42  # 初始y坐标
    count = 0  # 当前行的物品数量
    for item in img_list:
        img = item.get_img()  # 获取物品图片
        surface.blit(img, (x, y))  # 将图片绘制到surface上
        x += img.get_width() + 9  # 更新x坐标以便下一个图片不会覆盖当前图片
        count += 1  # 更新当前行的物品数量
        if count == items_per_row:  # 如果当前行的物品数量达到了6，就换行
            x = 368  # 重置x坐标
            y += img.get_height() + 16  # 更新y坐标以便下一个图片在新的一行
            count = 0  # 重置当前行的物品数量


def position_id(mx, my):
    x = 368
    y = 42
    count = 0
    for i in range(30):
        if x < mx < x + 89 and y < my < y + 91:
            #print (i)
            return i
        x += 89 + 9
        count += 1
        if count == 6:
            x = 368
            y += 91 + 16
            count = 0
    #print(-1)
    return -1

def print_text(surface, text, x, y, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)  # 设置文本矩形的左上角坐标
    surface.blit(text_surface, text_rect)

def print_title(surface, print_page):
    x = 45
    y = 100
    size = 40
    if print_page == 0:
        print_text(surface, "Weapon",   x, y, size, (0, 0, 0))
    elif print_page == 1:
        print_text(surface, "Armor",    x, y, size, (0, 0, 0))
    elif print_page == 2:
        print_text(surface, "Jewelry",  x, y, size, (0, 0, 0))

def print_info(surface, print_page, page, position_id):
    size = 26
    x = 45
    y = 150
    if position_id != -1:
        i = position_id + page * 30
        if print_page == 0 :
            weapons = load_items_from_file("weapons.pkl")
            if i < len(weapons):
                item = weapons[i]
                text_dict = item.to_dict()
                
                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20  # 更新y坐标以便下一个文本在新的一行
        elif print_page == 1 :
            armors = load_items_from_file("armors.pkl")
            if i < len(armors):
                item = armors[i]
                text_dict = item.to_dict()
                
                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20  # 更新y坐标以便下一个文本在新的一行
        elif print_page == 2 :
            jewelrys = load_items_from_file("jewelrys.pkl")
            if i < len(jewelrys):
                item = jewelrys[i]
                text_dict = item.to_dict()
                
                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20  # 更新y坐标以便下一个文本在新的一行
current_page = 0
print_page = 0
def page_change_click(self):
    global current_page
    if current_page >= 1 :
        current_page = current_page - 1
def page_change_plus(self):
    global current_page
    if current_page <= 18 :
        current_page = current_page+ 1
def page_change_box(self):
    global print_page
    if print_page !=0:
        pass
def backpack(surface):
    global current_page
    mx, my = 0, 0
    #page = 0
    from Ffloor import FirstFloor
    # 时钟
    clock = pygame.time.Clock()
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    page_font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 24)
    # image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"), (50, 50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"), (50, 50))
    pakage = pygame.transform.scale(pygame.image.load("./resource/character/inventory.png"), (1080, 600))
    left_page = pygame.transform.scale(pygame.image.load("./resource/background/button/left.png"), (100,100))
    right_page = pygame.transform.scale(pygame.image.load("./resource/background/button/right.png"), (100, 100))
    leftD_page = pygame.transform.scale(pygame.image.load("./resource/background/button/leftD.png"), (100,100))
    rightD_page = pygame.transform.scale(pygame.image.load("./resource/background/button/rightD.png"), (100,100))
    # 背包物品展示
    select_position_id = -1  # 选中的物品的索引
    print_page = 0  # 前选择页数当

    # button
    esc = TButton(1230, 0, " ", crossN, crossN, crossD, FirstFloor, font, (0, 0, 0))
    left = TButton(500, 600, " ", left_page,left_page,leftD_page,page_change_click,font,(0,0,0))
    right = TButton(600, 600, " ", right_page,right_page,rightD_page,page_change_plus,font,(0,0,0))
    running = True

    #event
    EVENT1 = pygame.USEREVENT
    pygame.time.set_timer(EVENT1, 1000)
    while running:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            position_id(mx, my)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx, my)
                left.getFocus(mx, my)
                right.getFocus(mx, my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    esc.mouseDown(mx, my)
                    left.mouseDown(mx, my)
                    right.mouseDown(mx, my)
                    if 900 < mx < 1000 and 600 < my < 700:
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
                left.mouseUp(mx, my)
                right.mouseUp(mx, my)
            elif event.type == EVENT1:
                pygame.display.update()

        red_rect = pygame.Rect(500, 600, 100, 100)
        green_rect = pygame.Rect(600, 600, 100, 100)
        blue_rect = pygame.Rect(900, 600, 100, 100)
        magenta_rect = pygame.Rect(1000, 600, 100, 100)



        pygame.draw.rect(screen, (255, 0, 0), red_rect, 2)
        pygame.draw.rect(screen, (0, 255, 0), green_rect, 2)
        pygame.draw.rect(screen, (0, 0, 255), blue_rect, 2)
        pygame.draw.rect(screen, (255, 0, 255), magenta_rect, 2)



        surface.blit(pakage, (0, 0))

        rect_x, rect_y, rect_width, rect_height = 350, 600, 100, 50
        pygame.draw.rect(surface, (196, 164, 132), [rect_x, rect_y, rect_width, rect_height])
        page_num_text = page_font.render(f'Page {current_page}', True, (255, 255, 255))
        text_rect = page_num_text.get_rect(center=(rect_x + rect_width / 2, rect_y + rect_height / 2))
        surface.blit(page_num_text, text_rect)

        esc.draw(screen)
        left.draw(screen)
        right.draw(screen)
        print_img(screen, print_page, current_page)
        print_title(screen, print_page)
        print_info(screen, print_page, current_page, position_id(mx, my))
        pygame.display.flip()
        clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((1280, 800))

if __name__ == '__main__':
    backpack(screen)
